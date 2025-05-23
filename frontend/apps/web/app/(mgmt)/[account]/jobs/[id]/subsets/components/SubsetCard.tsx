import {
  ConnectionConfigCase,
  getConnectionType,
} from '@/app/(mgmt)/[account]/connections/util';
import { SubsetFormValues } from '@/app/(mgmt)/[account]/new/job/job-form-validations';
import SubsetOptionsForm from '@/components/jobs/Form/SubsetOptionsForm';
import EditItem from '@/components/jobs/subsets/edit/EditItem';
import EditItemDialog from '@/components/jobs/subsets/edit/EditItemDialog';
import EditItems from '@/components/jobs/subsets/edit/EditItems';
import useOnBulkEditItemSave, {
  BulkEditItem,
} from '@/components/jobs/subsets/edit/useOnBulkEditItemSave';
import useOnEditItemSave from '@/components/jobs/subsets/edit/useOnEditItemSave';
import {
  SUBSET_TABLE_COLUMNS,
  SubsetTableRow,
} from '@/components/jobs/subsets/SubsetTable/Columns';
import SubsetTable from '@/components/jobs/subsets/SubsetTable/SubsetTable';
import {
  buildRowKey,
  buildTableRowData,
  getBulkColumnsForSqlAutocomplete,
  getColumnsForSqlAutocomplete,
  isValidSubsetType,
} from '@/components/jobs/subsets/utils';
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert';
import { Button } from '@/components/ui/button';
import { Form } from '@/components/ui/form';
import { getErrorMessage } from '@/util/util';
import { create } from '@bufbuild/protobuf';
import {
  createConnectQueryKey,
  useMutation,
  useQuery,
} from '@connectrpc/connect-query';
import { yupResolver } from '@hookform/resolvers/yup';
import {
  ConnectionConfigSchema,
  ConnectionDataService,
  ConnectionService,
  GetJobResponseSchema,
  JobService,
  JobSourceOptions,
} from '@neosync/sdk';
import { ExclamationTriangleIcon } from '@radix-ui/react-icons';
import { useQueryClient } from '@tanstack/react-query';
import { ReactElement, useEffect, useMemo, useState } from 'react';
import { useFieldArray, useForm } from 'react-hook-form';
import { toast } from 'sonner';
import { toJobSourceSqlSubsetSchemas } from '../../../util';
import { getConnectionIdFromSource } from '../../source/components/util';
import SubsetSkeleton from './SubsetSkeleton';

interface Props {
  jobId: string;
}

export default function SubsetCard(props: Props): ReactElement {
  const { jobId } = props;
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [isBulkEditDialogOpen, setIsBulkEditDialogOpen] = useState(false);

  const { data, isLoading: isJobLoading } = useQuery(
    JobService.method.getJob,
    { id: jobId },
    { enabled: !!jobId }
  );
  const queryclient = useQueryClient();
  const sourceConnectionId = getConnectionIdFromSource(data?.job?.source);
  const { data: tableConstraints, isFetching: isTableConstraintsValidating } =
    useQuery(
      ConnectionDataService.method.getConnectionTableConstraints,
      { connectionId: sourceConnectionId },
      { enabled: !!sourceConnectionId }
    );
  const { mutateAsync: setJobSubsets } = useMutation(
    JobService.method.setJobSourceSqlConnectionSubsets
  );
  const { data: sourceConnectionData } = useQuery(
    ConnectionService.method.getConnection,
    { id: sourceConnectionId },
    { enabled: !!sourceConnectionId }
  );

  const fkConstraints = tableConstraints?.foreignKeyConstraints;

  const [rootTables, setRootTables] = useState<Set<string>>(new Set());

  useEffect(() => {
    if (!isTableConstraintsValidating && fkConstraints) {
      const newRootTables = new Set(rootTables);
      data?.job?.mappings.forEach((m) => {
        const tn = `${m.schema}.${m.table}`;
        if (!fkConstraints[tn]) {
          newRootTables.add(tn);
        }
      });
      setRootTables(newRootTables);
    }
  }, [fkConstraints, isTableConstraintsValidating]);

  const formValues = getFormValues(data?.job?.source?.options);
  const form = useForm({
    resolver: yupResolver<SubsetFormValues>(SubsetFormValues),
    defaultValues: { subsets: [] },
    values: formValues,
  });

  const formSubsets = form.watch().subsets; // ensures that all form changes cause a re-render since stuff happens outside of the form that depends on the form values
  const { update: updateSubsetsFormValues, append: addSubsetsFormValues } =
    useFieldArray({
      control: form.control,
      name: 'subsets',
    });
  const [itemToEdit, setItemToEdit] = useState<SubsetTableRow | undefined>();
  const [bulkItemEdit, setBulkItemEdit] = useState<BulkEditItem | undefined>();

  const tableRowData = useMemo(() => {
    return buildTableRowData(
      data?.job?.mappings ?? [],
      rootTables,
      formSubsets
    );
  }, [data?.job?.mappings, rootTables, formSubsets]);

  const { onClick: onEditItemSave } = useOnEditItemSave({
    item: itemToEdit,
    getSubsets: () => formSubsets,
    appendSubsets: addSubsetsFormValues,
    triggerUpdate: () => {
      form.trigger();
      setIsDialogOpen(false);
      setItemToEdit(undefined);
    },
    updateSubset: (idx, subset) => {
      updateSubsetsFormValues(idx, subset);
    },
  });

  const { onClick: onBulkEditItemSave } = useOnBulkEditItemSave({
    bulkEditItem: bulkItemEdit,
    getSubsets: () => formSubsets,
    setSubsets: () => {
      form.setValue('subsets', formSubsets, {
        shouldDirty: true,
        shouldTouch: true,
        shouldValidate: false,
      });
    },
    triggerUpdate: () => {
      form.trigger();
      setIsBulkEditDialogOpen(false);
      setBulkItemEdit(undefined);
    },
    getTableRowData: (key) => tableRowData[key],
    appendSubsets: addSubsetsFormValues,
  });

  const formValuesMap = new Map(
    formValues.subsets.map((ss) => [buildRowKey(ss.schema, ss.table), ss])
  );

  const sqlAutocompleteColumns = useMemo(() => {
    return getColumnsForSqlAutocomplete(
      data?.job?.mappings ?? [],
      itemToEdit?.schema ?? '',
      itemToEdit?.table ?? ''
    );
  }, [data?.job?.mappings, itemToEdit?.schema, itemToEdit?.table]);

  const bulkSqlAutocompleteColumns = useMemo(() => {
    if (!bulkItemEdit) {
      return [];
    }
    return getBulkColumnsForSqlAutocomplete(
      data?.job?.mappings ?? [],
      bulkItemEdit.rowKeys.map((key) => {
        const td = tableRowData[key];
        if (!td) {
          return { schema: '', table: '' };
        }
        return {
          schema: td.schema,
          table: td.table,
        };
      }) ?? []
    );
  }, [data?.job?.mappings, bulkItemEdit?.rowKeys, tableRowData]);

  if (isJobLoading) {
    return (
      <div className="space-y-10">
        <SubsetSkeleton />
      </div>
    );
  }

  const connectionType = getConnectionType(
    sourceConnectionData?.connection?.connectionConfig ??
      create(ConnectionConfigSchema)
  );

  if (!isValidSubsetType(connectionType)) {
    return (
      <Alert variant="warning">
        <ExclamationTriangleIcon className="h-4 w-4" />
        <AlertTitle>Heads up!</AlertTitle>
        <AlertDescription>
          The source connection configured does not currently support
          subsettings
        </AlertDescription>
      </Alert>
    );
  }

  async function onSubmit(values: SubsetFormValues): Promise<void> {
    if (!isValidSubsetType(connectionType)) {
      return;
    }

    try {
      const updatedJobRes = await setJobSubsets({
        id: jobId,
        subsetByForeignKeyConstraints:
          values.subsetOptions.subsetByForeignKeyConstraints,
        schemas: toJobSourceSqlSubsetSchemas(values, connectionType),
      });
      toast.success('Successfully updated database subsets');
      queryclient.setQueryData(
        createConnectQueryKey({
          schema: JobService.method.getJob,
          input: { id: updatedJobRes.job?.id },
          cardinality: undefined,
        }),
        create(GetJobResponseSchema, { job: updatedJobRes.job })
      );
    } catch (err) {
      console.error(err);
      toast.error('Unable to update database subsets', {
        description: getErrorMessage(err),
      });
    }
  }

  function hasLocalChange(
    _rowIdx: number,
    schema: string,
    table: string
  ): boolean {
    const key = buildRowKey(schema, table);
    const trData = tableRowData[key];

    const svrData = formValuesMap.get(key);

    if (!svrData && !!trData.where) {
      return true;
    }

    return trData.where !== svrData?.whereClause;
  }

  function onLocalRowReset(
    _rowIdx: number,
    schema: string,
    table: string
  ): void {
    const key = buildRowKey(schema, table);
    const idx = form
      .getValues()
      .subsets.findIndex(
        (item) => buildRowKey(item.schema, item.table) === key
      );
    if (idx >= 0) {
      const svrData = formValuesMap.get(key);
      updateSubsetsFormValues(idx, {
        schema: schema,
        table: table,
        whereClause: svrData?.whereClause ?? undefined,
      });
    }
  }

  function onEdit(_rowIdx: number, schema: string, table: string): void {
    setIsDialogOpen(true);
    const key = buildRowKey(schema, table);
    if (tableRowData[key]) {
      setItemToEdit({
        ...tableRowData[key],
      });
    }
  }

  function onBulkEdit(
    data: SubsetTableRow[],
    onClearSelection: () => void
  ): void {
    // todo: if only one item is selected, just go through the single item flow
    if (data.length === 0) {
      return;
    }
    if (data.length === 1) {
      onEdit(0, data[0].schema, data[0].table);
      return;
    }
    const firstWhereClauseIdx = data.findIndex((item) => !!item.where);
    setBulkItemEdit({
      rowKeys: data.map((item) => buildRowKey(item.schema, item.table)),
      item: {
        where: firstWhereClauseIdx >= 0 ? data[firstWhereClauseIdx].where : '',
      },
      onClearSelection,
    });
    setIsBulkEditDialogOpen(true);
  }

  return (
    <div>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="flex flex-col">
          {showSubsetOptions(connectionType) && (
            <SubsetOptionsForm maxColNum={2} />
          )}
          <div className="flex flex-col gap-2">
            <div>
              <SubsetTable
                data={Object.values(tableRowData)}
                columns={SUBSET_TABLE_COLUMNS}
                onEdit={onEdit}
                onBulkEdit={onBulkEdit}
                hasLocalChange={hasLocalChange}
                onReset={onLocalRowReset}
              />
            </div>

            <EditItemDialog
              open={isDialogOpen}
              onOpenChange={setIsDialogOpen}
              body={
                <EditItem
                  connectionId={sourceConnectionId ?? ''}
                  item={itemToEdit}
                  onItem={setItemToEdit}
                  onCancel={() => {
                    setItemToEdit(undefined);
                    setIsDialogOpen(false);
                  }}
                  columns={sqlAutocompleteColumns}
                  onSave={onEditItemSave}
                  connectionType={connectionType}
                />
              }
            />
            <EditItemDialog
              open={isBulkEditDialogOpen}
              onOpenChange={setIsBulkEditDialogOpen}
              body={
                <EditItems
                  item={bulkItemEdit?.item ?? { where: '' }}
                  onItem={(item) => {
                    setBulkItemEdit((prev) => {
                      if (!prev) {
                        return undefined;
                      }
                      return {
                        ...prev,
                        item,
                      };
                    });
                  }}
                  onCancel={() => {
                    setBulkItemEdit(undefined);
                    setIsBulkEditDialogOpen(false);
                  }}
                  columns={bulkSqlAutocompleteColumns}
                  onSave={onBulkEditItemSave}
                />
              }
            />
            <div className="flex flex-row pt-10 justify-end">
              <Button key="submit" type="submit">
                Save
              </Button>
            </div>
          </div>
        </form>
      </Form>
    </div>
  );
}

// Determines if the subset options should be wholesale shown
// May need to change this in the future if a subset of the options apply to specific source connections.
// Currently there is only one and it only applies to pg/mysql
export function showSubsetOptions(
  connType: ConnectionConfigCase | null
): boolean {
  return (
    connType === 'pgConfig' ||
    connType === 'mysqlConfig' ||
    connType === 'mssqlConfig'
  );
}

function getFormValues(sourceOpts?: JobSourceOptions): SubsetFormValues {
  switch (sourceOpts?.config.case) {
    case 'postgres':
    case 'mysql':
    case 'mssql': {
      const schemas = sourceOpts.config.value.schemas;
      const subsets: SubsetFormValues['subsets'] = schemas.flatMap((schema) => {
        return schema.tables.map((table) => {
          return {
            schema: schema.schema,
            table: table.table,
            whereClause: table.whereClause,
          };
        });
      });
      return {
        subsets,
        subsetOptions: {
          subsetByForeignKeyConstraints:
            sourceOpts.config.value.subsetByForeignKeyConstraints,
        },
      };
    }
    case 'dynamodb': {
      const tables = sourceOpts.config.value.tables;
      const subsets: SubsetFormValues['subsets'] = tables.map((tableOpt) => {
        return {
          schema: 'dynamodb',
          table: tableOpt.table,
          whereClause: tableOpt.whereClause,
        };
      });
      return {
        subsets,
        subsetOptions: {
          subsetByForeignKeyConstraints: false,
        },
      };
    }
    default: {
      return {
        subsets: [],
        subsetOptions: { subsetByForeignKeyConstraints: false },
      };
    }
  }
}
