from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from mgmt.v1alpha1 import connection_data_pb2 as _connection_data_pb2
from mgmt.v1alpha1 import transformer_pb2 as _transformer_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JobStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOB_STATUS_UNSPECIFIED: _ClassVar[JobStatus]
    JOB_STATUS_ENABLED: _ClassVar[JobStatus]
    JOB_STATUS_PAUSED: _ClassVar[JobStatus]
    JOB_STATUS_DISABLED: _ClassVar[JobStatus]

class ActivityStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTIVITY_STATUS_UNSPECIFIED: _ClassVar[ActivityStatus]
    ACTIVITY_STATUS_SCHEDULED: _ClassVar[ActivityStatus]
    ACTIVITY_STATUS_STARTED: _ClassVar[ActivityStatus]
    ACTIVITY_STATUS_CANCELED: _ClassVar[ActivityStatus]
    ACTIVITY_STATUS_FAILED: _ClassVar[ActivityStatus]

class JobRunStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOB_RUN_STATUS_UNSPECIFIED: _ClassVar[JobRunStatus]
    JOB_RUN_STATUS_PENDING: _ClassVar[JobRunStatus]
    JOB_RUN_STATUS_RUNNING: _ClassVar[JobRunStatus]
    JOB_RUN_STATUS_COMPLETE: _ClassVar[JobRunStatus]
    JOB_RUN_STATUS_ERROR: _ClassVar[JobRunStatus]
    JOB_RUN_STATUS_CANCELED: _ClassVar[JobRunStatus]
    JOB_RUN_STATUS_TERMINATED: _ClassVar[JobRunStatus]
    JOB_RUN_STATUS_FAILED: _ClassVar[JobRunStatus]
    JOB_RUN_STATUS_TIMED_OUT: _ClassVar[JobRunStatus]

class LogWindow(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOG_WINDOW_NO_TIME_UNSPECIFIED: _ClassVar[LogWindow]
    LOG_WINDOW_FIFTEEN_MIN: _ClassVar[LogWindow]
    LOG_WINDOW_ONE_HOUR: _ClassVar[LogWindow]
    LOG_WINDOW_ONE_DAY: _ClassVar[LogWindow]

class LogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOG_LEVEL_UNSPECIFIED: _ClassVar[LogLevel]
    LOG_LEVEL_DEBUG: _ClassVar[LogLevel]
    LOG_LEVEL_INFO: _ClassVar[LogLevel]
    LOG_LEVEL_WARN: _ClassVar[LogLevel]
    LOG_LEVEL_ERROR: _ClassVar[LogLevel]
JOB_STATUS_UNSPECIFIED: JobStatus
JOB_STATUS_ENABLED: JobStatus
JOB_STATUS_PAUSED: JobStatus
JOB_STATUS_DISABLED: JobStatus
ACTIVITY_STATUS_UNSPECIFIED: ActivityStatus
ACTIVITY_STATUS_SCHEDULED: ActivityStatus
ACTIVITY_STATUS_STARTED: ActivityStatus
ACTIVITY_STATUS_CANCELED: ActivityStatus
ACTIVITY_STATUS_FAILED: ActivityStatus
JOB_RUN_STATUS_UNSPECIFIED: JobRunStatus
JOB_RUN_STATUS_PENDING: JobRunStatus
JOB_RUN_STATUS_RUNNING: JobRunStatus
JOB_RUN_STATUS_COMPLETE: JobRunStatus
JOB_RUN_STATUS_ERROR: JobRunStatus
JOB_RUN_STATUS_CANCELED: JobRunStatus
JOB_RUN_STATUS_TERMINATED: JobRunStatus
JOB_RUN_STATUS_FAILED: JobRunStatus
JOB_RUN_STATUS_TIMED_OUT: JobRunStatus
LOG_WINDOW_NO_TIME_UNSPECIFIED: LogWindow
LOG_WINDOW_FIFTEEN_MIN: LogWindow
LOG_WINDOW_ONE_HOUR: LogWindow
LOG_WINDOW_ONE_DAY: LogWindow
LOG_LEVEL_UNSPECIFIED: LogLevel
LOG_LEVEL_DEBUG: LogLevel
LOG_LEVEL_INFO: LogLevel
LOG_LEVEL_WARN: LogLevel
LOG_LEVEL_ERROR: LogLevel

class GetJobsRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class GetJobsResponse(_message.Message):
    __slots__ = ("jobs",)
    JOBS_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[Job]
    def __init__(self, jobs: _Optional[_Iterable[_Union[Job, _Mapping]]] = ...) -> None: ...

class JobSource(_message.Message):
    __slots__ = ("options",)
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: JobSourceOptions
    def __init__(self, options: _Optional[_Union[JobSourceOptions, _Mapping]] = ...) -> None: ...

class JobSourceOptions(_message.Message):
    __slots__ = ("postgres", "aws_s3", "mysql", "generate", "ai_generate", "mongodb", "dynamodb", "mssql")
    POSTGRES_FIELD_NUMBER: _ClassVar[int]
    AWS_S3_FIELD_NUMBER: _ClassVar[int]
    MYSQL_FIELD_NUMBER: _ClassVar[int]
    GENERATE_FIELD_NUMBER: _ClassVar[int]
    AI_GENERATE_FIELD_NUMBER: _ClassVar[int]
    MONGODB_FIELD_NUMBER: _ClassVar[int]
    DYNAMODB_FIELD_NUMBER: _ClassVar[int]
    MSSQL_FIELD_NUMBER: _ClassVar[int]
    postgres: PostgresSourceConnectionOptions
    aws_s3: AwsS3SourceConnectionOptions
    mysql: MysqlSourceConnectionOptions
    generate: GenerateSourceOptions
    ai_generate: AiGenerateSourceOptions
    mongodb: MongoDBSourceConnectionOptions
    dynamodb: DynamoDBSourceConnectionOptions
    mssql: MssqlSourceConnectionOptions
    def __init__(self, postgres: _Optional[_Union[PostgresSourceConnectionOptions, _Mapping]] = ..., aws_s3: _Optional[_Union[AwsS3SourceConnectionOptions, _Mapping]] = ..., mysql: _Optional[_Union[MysqlSourceConnectionOptions, _Mapping]] = ..., generate: _Optional[_Union[GenerateSourceOptions, _Mapping]] = ..., ai_generate: _Optional[_Union[AiGenerateSourceOptions, _Mapping]] = ..., mongodb: _Optional[_Union[MongoDBSourceConnectionOptions, _Mapping]] = ..., dynamodb: _Optional[_Union[DynamoDBSourceConnectionOptions, _Mapping]] = ..., mssql: _Optional[_Union[MssqlSourceConnectionOptions, _Mapping]] = ...) -> None: ...

class CreateJobDestination(_message.Message):
    __slots__ = ("connection_id", "options")
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    options: JobDestinationOptions
    def __init__(self, connection_id: _Optional[str] = ..., options: _Optional[_Union[JobDestinationOptions, _Mapping]] = ...) -> None: ...

class JobDestination(_message.Message):
    __slots__ = ("connection_id", "options", "id")
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    options: JobDestinationOptions
    id: str
    def __init__(self, connection_id: _Optional[str] = ..., options: _Optional[_Union[JobDestinationOptions, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class AiGenerateSourceOptions(_message.Message):
    __slots__ = ("ai_connection_id", "schemas", "fk_source_connection_id", "model_name", "user_prompt", "generate_batch_size")
    AI_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    FK_SOURCE_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    GENERATE_BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    ai_connection_id: str
    schemas: _containers.RepeatedCompositeFieldContainer[AiGenerateSourceSchemaOption]
    fk_source_connection_id: str
    model_name: str
    user_prompt: str
    generate_batch_size: int
    def __init__(self, ai_connection_id: _Optional[str] = ..., schemas: _Optional[_Iterable[_Union[AiGenerateSourceSchemaOption, _Mapping]]] = ..., fk_source_connection_id: _Optional[str] = ..., model_name: _Optional[str] = ..., user_prompt: _Optional[str] = ..., generate_batch_size: _Optional[int] = ...) -> None: ...

class AiGenerateSourceSchemaOption(_message.Message):
    __slots__ = ("schema", "tables")
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    schema: str
    tables: _containers.RepeatedCompositeFieldContainer[AiGenerateSourceTableOption]
    def __init__(self, schema: _Optional[str] = ..., tables: _Optional[_Iterable[_Union[AiGenerateSourceTableOption, _Mapping]]] = ...) -> None: ...

class AiGenerateSourceTableOption(_message.Message):
    __slots__ = ("table", "row_count")
    TABLE_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    table: str
    row_count: int
    def __init__(self, table: _Optional[str] = ..., row_count: _Optional[int] = ...) -> None: ...

class GenerateSourceOptions(_message.Message):
    __slots__ = ("schemas", "fk_source_connection_id")
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    FK_SOURCE_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    schemas: _containers.RepeatedCompositeFieldContainer[GenerateSourceSchemaOption]
    fk_source_connection_id: str
    def __init__(self, schemas: _Optional[_Iterable[_Union[GenerateSourceSchemaOption, _Mapping]]] = ..., fk_source_connection_id: _Optional[str] = ...) -> None: ...

class GenerateSourceSchemaOption(_message.Message):
    __slots__ = ("schema", "tables")
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    schema: str
    tables: _containers.RepeatedCompositeFieldContainer[GenerateSourceTableOption]
    def __init__(self, schema: _Optional[str] = ..., tables: _Optional[_Iterable[_Union[GenerateSourceTableOption, _Mapping]]] = ...) -> None: ...

class GenerateSourceTableOption(_message.Message):
    __slots__ = ("table", "row_count")
    TABLE_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    table: str
    row_count: int
    def __init__(self, table: _Optional[str] = ..., row_count: _Optional[int] = ...) -> None: ...

class MongoDBSourceConnectionOptions(_message.Message):
    __slots__ = ("connection_id",)
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    def __init__(self, connection_id: _Optional[str] = ...) -> None: ...

class DynamoDBSourceConnectionOptions(_message.Message):
    __slots__ = ("connection_id", "tables", "unmapped_transforms", "enable_consistent_read")
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    UNMAPPED_TRANSFORMS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CONSISTENT_READ_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    tables: _containers.RepeatedCompositeFieldContainer[DynamoDBSourceTableOption]
    unmapped_transforms: DynamoDBSourceUnmappedTransformConfig
    enable_consistent_read: bool
    def __init__(self, connection_id: _Optional[str] = ..., tables: _Optional[_Iterable[_Union[DynamoDBSourceTableOption, _Mapping]]] = ..., unmapped_transforms: _Optional[_Union[DynamoDBSourceUnmappedTransformConfig, _Mapping]] = ..., enable_consistent_read: bool = ...) -> None: ...

class DynamoDBSourceUnmappedTransformConfig(_message.Message):
    __slots__ = ("b", "boolean", "n", "s")
    B_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    S_FIELD_NUMBER: _ClassVar[int]
    b: JobMappingTransformer
    boolean: JobMappingTransformer
    n: JobMappingTransformer
    s: JobMappingTransformer
    def __init__(self, b: _Optional[_Union[JobMappingTransformer, _Mapping]] = ..., boolean: _Optional[_Union[JobMappingTransformer, _Mapping]] = ..., n: _Optional[_Union[JobMappingTransformer, _Mapping]] = ..., s: _Optional[_Union[JobMappingTransformer, _Mapping]] = ...) -> None: ...

class DynamoDBSourceTableOption(_message.Message):
    __slots__ = ("table", "where_clause")
    TABLE_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    table: str
    where_clause: str
    def __init__(self, table: _Optional[str] = ..., where_clause: _Optional[str] = ...) -> None: ...

class PostgresSourceConnectionOptions(_message.Message):
    __slots__ = ("schemas", "connection_id", "subset_by_foreign_key_constraints", "new_column_addition_strategy", "column_removal_strategy")
    class NewColumnAdditionStrategy(_message.Message):
        __slots__ = ("halt_job", "auto_map", "passthrough")
        class HaltJob(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class AutoMap(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Passthrough(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        HALT_JOB_FIELD_NUMBER: _ClassVar[int]
        AUTO_MAP_FIELD_NUMBER: _ClassVar[int]
        PASSTHROUGH_FIELD_NUMBER: _ClassVar[int]
        halt_job: PostgresSourceConnectionOptions.NewColumnAdditionStrategy.HaltJob
        auto_map: PostgresSourceConnectionOptions.NewColumnAdditionStrategy.AutoMap
        passthrough: PostgresSourceConnectionOptions.NewColumnAdditionStrategy.Passthrough
        def __init__(self, halt_job: _Optional[_Union[PostgresSourceConnectionOptions.NewColumnAdditionStrategy.HaltJob, _Mapping]] = ..., auto_map: _Optional[_Union[PostgresSourceConnectionOptions.NewColumnAdditionStrategy.AutoMap, _Mapping]] = ..., passthrough: _Optional[_Union[PostgresSourceConnectionOptions.NewColumnAdditionStrategy.Passthrough, _Mapping]] = ...) -> None: ...
    class ColumnRemovalStrategy(_message.Message):
        __slots__ = ("halt_job", "continue_job")
        class HaltJob(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ContinueJob(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        HALT_JOB_FIELD_NUMBER: _ClassVar[int]
        CONTINUE_JOB_FIELD_NUMBER: _ClassVar[int]
        halt_job: PostgresSourceConnectionOptions.ColumnRemovalStrategy.HaltJob
        continue_job: PostgresSourceConnectionOptions.ColumnRemovalStrategy.ContinueJob
        def __init__(self, halt_job: _Optional[_Union[PostgresSourceConnectionOptions.ColumnRemovalStrategy.HaltJob, _Mapping]] = ..., continue_job: _Optional[_Union[PostgresSourceConnectionOptions.ColumnRemovalStrategy.ContinueJob, _Mapping]] = ...) -> None: ...
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSET_BY_FOREIGN_KEY_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    NEW_COLUMN_ADDITION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    COLUMN_REMOVAL_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    schemas: _containers.RepeatedCompositeFieldContainer[PostgresSourceSchemaOption]
    connection_id: str
    subset_by_foreign_key_constraints: bool
    new_column_addition_strategy: PostgresSourceConnectionOptions.NewColumnAdditionStrategy
    column_removal_strategy: PostgresSourceConnectionOptions.ColumnRemovalStrategy
    def __init__(self, schemas: _Optional[_Iterable[_Union[PostgresSourceSchemaOption, _Mapping]]] = ..., connection_id: _Optional[str] = ..., subset_by_foreign_key_constraints: bool = ..., new_column_addition_strategy: _Optional[_Union[PostgresSourceConnectionOptions.NewColumnAdditionStrategy, _Mapping]] = ..., column_removal_strategy: _Optional[_Union[PostgresSourceConnectionOptions.ColumnRemovalStrategy, _Mapping]] = ...) -> None: ...

class PostgresSourceSchemaOption(_message.Message):
    __slots__ = ("schema", "tables")
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    schema: str
    tables: _containers.RepeatedCompositeFieldContainer[PostgresSourceTableOption]
    def __init__(self, schema: _Optional[str] = ..., tables: _Optional[_Iterable[_Union[PostgresSourceTableOption, _Mapping]]] = ...) -> None: ...

class PostgresSourceTableOption(_message.Message):
    __slots__ = ("table", "where_clause")
    TABLE_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    table: str
    where_clause: str
    def __init__(self, table: _Optional[str] = ..., where_clause: _Optional[str] = ...) -> None: ...

class MysqlSourceConnectionOptions(_message.Message):
    __slots__ = ("halt_on_new_column_addition", "schemas", "connection_id", "subset_by_foreign_key_constraints", "column_removal_strategy", "new_column_addition_strategy")
    class ColumnRemovalStrategy(_message.Message):
        __slots__ = ("halt_job", "continue_job")
        class HaltJob(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ContinueJob(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        HALT_JOB_FIELD_NUMBER: _ClassVar[int]
        CONTINUE_JOB_FIELD_NUMBER: _ClassVar[int]
        halt_job: MysqlSourceConnectionOptions.ColumnRemovalStrategy.HaltJob
        continue_job: MysqlSourceConnectionOptions.ColumnRemovalStrategy.ContinueJob
        def __init__(self, halt_job: _Optional[_Union[MysqlSourceConnectionOptions.ColumnRemovalStrategy.HaltJob, _Mapping]] = ..., continue_job: _Optional[_Union[MysqlSourceConnectionOptions.ColumnRemovalStrategy.ContinueJob, _Mapping]] = ...) -> None: ...
    class NewColumnAdditionStrategy(_message.Message):
        __slots__ = ("halt_job", "auto_map", "passthrough")
        class HaltJob(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class AutoMap(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Passthrough(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        HALT_JOB_FIELD_NUMBER: _ClassVar[int]
        AUTO_MAP_FIELD_NUMBER: _ClassVar[int]
        PASSTHROUGH_FIELD_NUMBER: _ClassVar[int]
        halt_job: MysqlSourceConnectionOptions.NewColumnAdditionStrategy.HaltJob
        auto_map: MysqlSourceConnectionOptions.NewColumnAdditionStrategy.AutoMap
        passthrough: MysqlSourceConnectionOptions.NewColumnAdditionStrategy.Passthrough
        def __init__(self, halt_job: _Optional[_Union[MysqlSourceConnectionOptions.NewColumnAdditionStrategy.HaltJob, _Mapping]] = ..., auto_map: _Optional[_Union[MysqlSourceConnectionOptions.NewColumnAdditionStrategy.AutoMap, _Mapping]] = ..., passthrough: _Optional[_Union[MysqlSourceConnectionOptions.NewColumnAdditionStrategy.Passthrough, _Mapping]] = ...) -> None: ...
    HALT_ON_NEW_COLUMN_ADDITION_FIELD_NUMBER: _ClassVar[int]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSET_BY_FOREIGN_KEY_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    COLUMN_REMOVAL_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    NEW_COLUMN_ADDITION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    halt_on_new_column_addition: bool
    schemas: _containers.RepeatedCompositeFieldContainer[MysqlSourceSchemaOption]
    connection_id: str
    subset_by_foreign_key_constraints: bool
    column_removal_strategy: MysqlSourceConnectionOptions.ColumnRemovalStrategy
    new_column_addition_strategy: MysqlSourceConnectionOptions.NewColumnAdditionStrategy
    def __init__(self, halt_on_new_column_addition: bool = ..., schemas: _Optional[_Iterable[_Union[MysqlSourceSchemaOption, _Mapping]]] = ..., connection_id: _Optional[str] = ..., subset_by_foreign_key_constraints: bool = ..., column_removal_strategy: _Optional[_Union[MysqlSourceConnectionOptions.ColumnRemovalStrategy, _Mapping]] = ..., new_column_addition_strategy: _Optional[_Union[MysqlSourceConnectionOptions.NewColumnAdditionStrategy, _Mapping]] = ...) -> None: ...

class MysqlSourceSchemaOption(_message.Message):
    __slots__ = ("schema", "tables")
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    schema: str
    tables: _containers.RepeatedCompositeFieldContainer[MysqlSourceTableOption]
    def __init__(self, schema: _Optional[str] = ..., tables: _Optional[_Iterable[_Union[MysqlSourceTableOption, _Mapping]]] = ...) -> None: ...

class MysqlSourceTableOption(_message.Message):
    __slots__ = ("table", "where_clause")
    TABLE_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    table: str
    where_clause: str
    def __init__(self, table: _Optional[str] = ..., where_clause: _Optional[str] = ...) -> None: ...

class MssqlSourceConnectionOptions(_message.Message):
    __slots__ = ("halt_on_new_column_addition", "schemas", "connection_id", "subset_by_foreign_key_constraints", "column_removal_strategy", "new_column_addition_strategy")
    class ColumnRemovalStrategy(_message.Message):
        __slots__ = ("halt_job", "continue_job")
        class HaltJob(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ContinueJob(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        HALT_JOB_FIELD_NUMBER: _ClassVar[int]
        CONTINUE_JOB_FIELD_NUMBER: _ClassVar[int]
        halt_job: MssqlSourceConnectionOptions.ColumnRemovalStrategy.HaltJob
        continue_job: MssqlSourceConnectionOptions.ColumnRemovalStrategy.ContinueJob
        def __init__(self, halt_job: _Optional[_Union[MssqlSourceConnectionOptions.ColumnRemovalStrategy.HaltJob, _Mapping]] = ..., continue_job: _Optional[_Union[MssqlSourceConnectionOptions.ColumnRemovalStrategy.ContinueJob, _Mapping]] = ...) -> None: ...
    class NewColumnAdditionStrategy(_message.Message):
        __slots__ = ("halt_job", "passthrough")
        class HaltJob(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Passthrough(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        HALT_JOB_FIELD_NUMBER: _ClassVar[int]
        PASSTHROUGH_FIELD_NUMBER: _ClassVar[int]
        halt_job: MssqlSourceConnectionOptions.NewColumnAdditionStrategy.HaltJob
        passthrough: MssqlSourceConnectionOptions.NewColumnAdditionStrategy.Passthrough
        def __init__(self, halt_job: _Optional[_Union[MssqlSourceConnectionOptions.NewColumnAdditionStrategy.HaltJob, _Mapping]] = ..., passthrough: _Optional[_Union[MssqlSourceConnectionOptions.NewColumnAdditionStrategy.Passthrough, _Mapping]] = ...) -> None: ...
    HALT_ON_NEW_COLUMN_ADDITION_FIELD_NUMBER: _ClassVar[int]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSET_BY_FOREIGN_KEY_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    COLUMN_REMOVAL_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    NEW_COLUMN_ADDITION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    halt_on_new_column_addition: bool
    schemas: _containers.RepeatedCompositeFieldContainer[MssqlSourceSchemaOption]
    connection_id: str
    subset_by_foreign_key_constraints: bool
    column_removal_strategy: MssqlSourceConnectionOptions.ColumnRemovalStrategy
    new_column_addition_strategy: MssqlSourceConnectionOptions.NewColumnAdditionStrategy
    def __init__(self, halt_on_new_column_addition: bool = ..., schemas: _Optional[_Iterable[_Union[MssqlSourceSchemaOption, _Mapping]]] = ..., connection_id: _Optional[str] = ..., subset_by_foreign_key_constraints: bool = ..., column_removal_strategy: _Optional[_Union[MssqlSourceConnectionOptions.ColumnRemovalStrategy, _Mapping]] = ..., new_column_addition_strategy: _Optional[_Union[MssqlSourceConnectionOptions.NewColumnAdditionStrategy, _Mapping]] = ...) -> None: ...

class MssqlSourceSchemaOption(_message.Message):
    __slots__ = ("schema", "tables")
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    schema: str
    tables: _containers.RepeatedCompositeFieldContainer[MssqlSourceTableOption]
    def __init__(self, schema: _Optional[str] = ..., tables: _Optional[_Iterable[_Union[MssqlSourceTableOption, _Mapping]]] = ...) -> None: ...

class MssqlSourceTableOption(_message.Message):
    __slots__ = ("table", "where_clause")
    TABLE_FIELD_NUMBER: _ClassVar[int]
    WHERE_CLAUSE_FIELD_NUMBER: _ClassVar[int]
    table: str
    where_clause: str
    def __init__(self, table: _Optional[str] = ..., where_clause: _Optional[str] = ...) -> None: ...

class AwsS3SourceConnectionOptions(_message.Message):
    __slots__ = ("connection_id",)
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    connection_id: str
    def __init__(self, connection_id: _Optional[str] = ...) -> None: ...

class JobDestinationOptions(_message.Message):
    __slots__ = ("postgres_options", "aws_s3_options", "mysql_options", "mongodb_options", "gcp_cloudstorage_options", "dynamodb_options", "mssql_options")
    POSTGRES_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    AWS_S3_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    MYSQL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    MONGODB_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    GCP_CLOUDSTORAGE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DYNAMODB_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    MSSQL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    postgres_options: PostgresDestinationConnectionOptions
    aws_s3_options: AwsS3DestinationConnectionOptions
    mysql_options: MysqlDestinationConnectionOptions
    mongodb_options: MongoDBDestinationConnectionOptions
    gcp_cloudstorage_options: GcpCloudStorageDestinationConnectionOptions
    dynamodb_options: DynamoDBDestinationConnectionOptions
    mssql_options: MssqlDestinationConnectionOptions
    def __init__(self, postgres_options: _Optional[_Union[PostgresDestinationConnectionOptions, _Mapping]] = ..., aws_s3_options: _Optional[_Union[AwsS3DestinationConnectionOptions, _Mapping]] = ..., mysql_options: _Optional[_Union[MysqlDestinationConnectionOptions, _Mapping]] = ..., mongodb_options: _Optional[_Union[MongoDBDestinationConnectionOptions, _Mapping]] = ..., gcp_cloudstorage_options: _Optional[_Union[GcpCloudStorageDestinationConnectionOptions, _Mapping]] = ..., dynamodb_options: _Optional[_Union[DynamoDBDestinationConnectionOptions, _Mapping]] = ..., mssql_options: _Optional[_Union[MssqlDestinationConnectionOptions, _Mapping]] = ...) -> None: ...

class MongoDBDestinationConnectionOptions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GcpCloudStorageDestinationConnectionOptions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DynamoDBDestinationConnectionOptions(_message.Message):
    __slots__ = ("table_mappings",)
    TABLE_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    table_mappings: _containers.RepeatedCompositeFieldContainer[DynamoDBDestinationTableMapping]
    def __init__(self, table_mappings: _Optional[_Iterable[_Union[DynamoDBDestinationTableMapping, _Mapping]]] = ...) -> None: ...

class DynamoDBDestinationTableMapping(_message.Message):
    __slots__ = ("source_table", "destination_table")
    SOURCE_TABLE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_TABLE_FIELD_NUMBER: _ClassVar[int]
    source_table: str
    destination_table: str
    def __init__(self, source_table: _Optional[str] = ..., destination_table: _Optional[str] = ...) -> None: ...

class PostgresDestinationConnectionOptions(_message.Message):
    __slots__ = ("truncate_table", "init_table_schema", "on_conflict", "skip_foreign_key_violations", "batch", "max_in_flight")
    TRUNCATE_TABLE_FIELD_NUMBER: _ClassVar[int]
    INIT_TABLE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ON_CONFLICT_FIELD_NUMBER: _ClassVar[int]
    SKIP_FOREIGN_KEY_VIOLATIONS_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    MAX_IN_FLIGHT_FIELD_NUMBER: _ClassVar[int]
    truncate_table: PostgresTruncateTableConfig
    init_table_schema: bool
    on_conflict: PostgresOnConflictConfig
    skip_foreign_key_violations: bool
    batch: BatchConfig
    max_in_flight: int
    def __init__(self, truncate_table: _Optional[_Union[PostgresTruncateTableConfig, _Mapping]] = ..., init_table_schema: bool = ..., on_conflict: _Optional[_Union[PostgresOnConflictConfig, _Mapping]] = ..., skip_foreign_key_violations: bool = ..., batch: _Optional[_Union[BatchConfig, _Mapping]] = ..., max_in_flight: _Optional[int] = ...) -> None: ...

class PostgresOnConflictConfig(_message.Message):
    __slots__ = ("do_nothing", "nothing", "update")
    class PostgresOnConflictDoNothing(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class PostgresOnConflictUpdate(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    DO_NOTHING_FIELD_NUMBER: _ClassVar[int]
    NOTHING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    do_nothing: bool
    nothing: PostgresOnConflictConfig.PostgresOnConflictDoNothing
    update: PostgresOnConflictConfig.PostgresOnConflictUpdate
    def __init__(self, do_nothing: bool = ..., nothing: _Optional[_Union[PostgresOnConflictConfig.PostgresOnConflictDoNothing, _Mapping]] = ..., update: _Optional[_Union[PostgresOnConflictConfig.PostgresOnConflictUpdate, _Mapping]] = ...) -> None: ...

class PostgresTruncateTableConfig(_message.Message):
    __slots__ = ("truncate_before_insert", "cascade")
    TRUNCATE_BEFORE_INSERT_FIELD_NUMBER: _ClassVar[int]
    CASCADE_FIELD_NUMBER: _ClassVar[int]
    truncate_before_insert: bool
    cascade: bool
    def __init__(self, truncate_before_insert: bool = ..., cascade: bool = ...) -> None: ...

class MysqlDestinationConnectionOptions(_message.Message):
    __slots__ = ("truncate_table", "init_table_schema", "on_conflict", "skip_foreign_key_violations", "batch", "max_in_flight")
    TRUNCATE_TABLE_FIELD_NUMBER: _ClassVar[int]
    INIT_TABLE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ON_CONFLICT_FIELD_NUMBER: _ClassVar[int]
    SKIP_FOREIGN_KEY_VIOLATIONS_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    MAX_IN_FLIGHT_FIELD_NUMBER: _ClassVar[int]
    truncate_table: MysqlTruncateTableConfig
    init_table_schema: bool
    on_conflict: MysqlOnConflictConfig
    skip_foreign_key_violations: bool
    batch: BatchConfig
    max_in_flight: int
    def __init__(self, truncate_table: _Optional[_Union[MysqlTruncateTableConfig, _Mapping]] = ..., init_table_schema: bool = ..., on_conflict: _Optional[_Union[MysqlOnConflictConfig, _Mapping]] = ..., skip_foreign_key_violations: bool = ..., batch: _Optional[_Union[BatchConfig, _Mapping]] = ..., max_in_flight: _Optional[int] = ...) -> None: ...

class MysqlTruncateTableConfig(_message.Message):
    __slots__ = ("truncate_before_insert",)
    TRUNCATE_BEFORE_INSERT_FIELD_NUMBER: _ClassVar[int]
    truncate_before_insert: bool
    def __init__(self, truncate_before_insert: bool = ...) -> None: ...

class MysqlOnConflictConfig(_message.Message):
    __slots__ = ("do_nothing", "nothing", "update")
    class MysqlOnConflictDoNothing(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class MysqlOnConflictUpdate(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    DO_NOTHING_FIELD_NUMBER: _ClassVar[int]
    NOTHING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    do_nothing: bool
    nothing: MysqlOnConflictConfig.MysqlOnConflictDoNothing
    update: MysqlOnConflictConfig.MysqlOnConflictUpdate
    def __init__(self, do_nothing: bool = ..., nothing: _Optional[_Union[MysqlOnConflictConfig.MysqlOnConflictDoNothing, _Mapping]] = ..., update: _Optional[_Union[MysqlOnConflictConfig.MysqlOnConflictUpdate, _Mapping]] = ...) -> None: ...

class MssqlDestinationConnectionOptions(_message.Message):
    __slots__ = ("truncate_table", "init_table_schema", "on_conflict", "skip_foreign_key_violations", "batch", "max_in_flight")
    TRUNCATE_TABLE_FIELD_NUMBER: _ClassVar[int]
    INIT_TABLE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ON_CONFLICT_FIELD_NUMBER: _ClassVar[int]
    SKIP_FOREIGN_KEY_VIOLATIONS_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    MAX_IN_FLIGHT_FIELD_NUMBER: _ClassVar[int]
    truncate_table: MssqlTruncateTableConfig
    init_table_schema: bool
    on_conflict: MssqlOnConflictConfig
    skip_foreign_key_violations: bool
    batch: BatchConfig
    max_in_flight: int
    def __init__(self, truncate_table: _Optional[_Union[MssqlTruncateTableConfig, _Mapping]] = ..., init_table_schema: bool = ..., on_conflict: _Optional[_Union[MssqlOnConflictConfig, _Mapping]] = ..., skip_foreign_key_violations: bool = ..., batch: _Optional[_Union[BatchConfig, _Mapping]] = ..., max_in_flight: _Optional[int] = ...) -> None: ...

class MssqlTruncateTableConfig(_message.Message):
    __slots__ = ("truncate_before_insert",)
    TRUNCATE_BEFORE_INSERT_FIELD_NUMBER: _ClassVar[int]
    truncate_before_insert: bool
    def __init__(self, truncate_before_insert: bool = ...) -> None: ...

class MssqlOnConflictConfig(_message.Message):
    __slots__ = ("do_nothing",)
    DO_NOTHING_FIELD_NUMBER: _ClassVar[int]
    do_nothing: bool
    def __init__(self, do_nothing: bool = ...) -> None: ...

class AwsS3DestinationConnectionOptions(_message.Message):
    __slots__ = ("storage_class", "max_in_flight", "timeout", "batch")
    class StorageClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STORAGE_CLASS_UNSPECIFIED: _ClassVar[AwsS3DestinationConnectionOptions.StorageClass]
        STORAGE_CLASS_STANDARD: _ClassVar[AwsS3DestinationConnectionOptions.StorageClass]
        STORAGE_CLASS_REDUCED_REDUNDANCY: _ClassVar[AwsS3DestinationConnectionOptions.StorageClass]
        STORAGE_CLASS_GLACIER: _ClassVar[AwsS3DestinationConnectionOptions.StorageClass]
        STORAGE_CLASS_STANDARD_IA: _ClassVar[AwsS3DestinationConnectionOptions.StorageClass]
        STORAGE_CLASS_ONEZONE_IA: _ClassVar[AwsS3DestinationConnectionOptions.StorageClass]
        STORAGE_CLASS_INTELLIGENT_TIERING: _ClassVar[AwsS3DestinationConnectionOptions.StorageClass]
        STORAGE_CLASS_DEEP_ARCHIVE: _ClassVar[AwsS3DestinationConnectionOptions.StorageClass]
    STORAGE_CLASS_UNSPECIFIED: AwsS3DestinationConnectionOptions.StorageClass
    STORAGE_CLASS_STANDARD: AwsS3DestinationConnectionOptions.StorageClass
    STORAGE_CLASS_REDUCED_REDUNDANCY: AwsS3DestinationConnectionOptions.StorageClass
    STORAGE_CLASS_GLACIER: AwsS3DestinationConnectionOptions.StorageClass
    STORAGE_CLASS_STANDARD_IA: AwsS3DestinationConnectionOptions.StorageClass
    STORAGE_CLASS_ONEZONE_IA: AwsS3DestinationConnectionOptions.StorageClass
    STORAGE_CLASS_INTELLIGENT_TIERING: AwsS3DestinationConnectionOptions.StorageClass
    STORAGE_CLASS_DEEP_ARCHIVE: AwsS3DestinationConnectionOptions.StorageClass
    STORAGE_CLASS_FIELD_NUMBER: _ClassVar[int]
    MAX_IN_FLIGHT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    storage_class: AwsS3DestinationConnectionOptions.StorageClass
    max_in_flight: int
    timeout: str
    batch: BatchConfig
    def __init__(self, storage_class: _Optional[_Union[AwsS3DestinationConnectionOptions.StorageClass, str]] = ..., max_in_flight: _Optional[int] = ..., timeout: _Optional[str] = ..., batch: _Optional[_Union[BatchConfig, _Mapping]] = ...) -> None: ...

class BatchConfig(_message.Message):
    __slots__ = ("count", "period")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    count: int
    period: str
    def __init__(self, count: _Optional[int] = ..., period: _Optional[str] = ...) -> None: ...

class CreateJobRequest(_message.Message):
    __slots__ = ("account_id", "job_name", "cron_schedule", "mappings", "source", "destinations", "initiate_job_run", "workflow_options", "sync_options", "virtual_foreign_keys", "job_type")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_NAME_FIELD_NUMBER: _ClassVar[int]
    CRON_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    INITIATE_JOB_RUN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SYNC_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_FOREIGN_KEYS_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    job_name: str
    cron_schedule: str
    mappings: _containers.RepeatedCompositeFieldContainer[JobMapping]
    source: JobSource
    destinations: _containers.RepeatedCompositeFieldContainer[CreateJobDestination]
    initiate_job_run: bool
    workflow_options: WorkflowOptions
    sync_options: ActivityOptions
    virtual_foreign_keys: _containers.RepeatedCompositeFieldContainer[VirtualForeignConstraint]
    job_type: JobTypeConfig
    def __init__(self, account_id: _Optional[str] = ..., job_name: _Optional[str] = ..., cron_schedule: _Optional[str] = ..., mappings: _Optional[_Iterable[_Union[JobMapping, _Mapping]]] = ..., source: _Optional[_Union[JobSource, _Mapping]] = ..., destinations: _Optional[_Iterable[_Union[CreateJobDestination, _Mapping]]] = ..., initiate_job_run: bool = ..., workflow_options: _Optional[_Union[WorkflowOptions, _Mapping]] = ..., sync_options: _Optional[_Union[ActivityOptions, _Mapping]] = ..., virtual_foreign_keys: _Optional[_Iterable[_Union[VirtualForeignConstraint, _Mapping]]] = ..., job_type: _Optional[_Union[JobTypeConfig, _Mapping]] = ...) -> None: ...

class JobTypeConfig(_message.Message):
    __slots__ = ("sync", "pii_detect")
    class JobTypeSync(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class JobTypePiiDetect(_message.Message):
        __slots__ = ("data_sampling", "table_scan_filter", "user_prompt", "incremental")
        class Incremental(_message.Message):
            __slots__ = ("is_enabled",)
            IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
            is_enabled: bool
            def __init__(self, is_enabled: bool = ...) -> None: ...
        class DataSampling(_message.Message):
            __slots__ = ("is_enabled",)
            IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
            is_enabled: bool
            def __init__(self, is_enabled: bool = ...) -> None: ...
        class TableScanFilter(_message.Message):
            __slots__ = ("include_all", "include", "exclude")
            INCLUDE_ALL_FIELD_NUMBER: _ClassVar[int]
            INCLUDE_FIELD_NUMBER: _ClassVar[int]
            EXCLUDE_FIELD_NUMBER: _ClassVar[int]
            include_all: JobTypeConfig.JobTypePiiDetect.IncludeAll
            include: JobTypeConfig.JobTypePiiDetect.TablePatterns
            exclude: JobTypeConfig.JobTypePiiDetect.TablePatterns
            def __init__(self, include_all: _Optional[_Union[JobTypeConfig.JobTypePiiDetect.IncludeAll, _Mapping]] = ..., include: _Optional[_Union[JobTypeConfig.JobTypePiiDetect.TablePatterns, _Mapping]] = ..., exclude: _Optional[_Union[JobTypeConfig.JobTypePiiDetect.TablePatterns, _Mapping]] = ...) -> None: ...
        class IncludeAll(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class TablePatterns(_message.Message):
            __slots__ = ("schemas", "tables")
            SCHEMAS_FIELD_NUMBER: _ClassVar[int]
            TABLES_FIELD_NUMBER: _ClassVar[int]
            schemas: _containers.RepeatedScalarFieldContainer[str]
            tables: _containers.RepeatedCompositeFieldContainer[JobTypeConfig.JobTypePiiDetect.TableIdentifier]
            def __init__(self, schemas: _Optional[_Iterable[str]] = ..., tables: _Optional[_Iterable[_Union[JobTypeConfig.JobTypePiiDetect.TableIdentifier, _Mapping]]] = ...) -> None: ...
        class TableIdentifier(_message.Message):
            __slots__ = ("schema", "table")
            SCHEMA_FIELD_NUMBER: _ClassVar[int]
            TABLE_FIELD_NUMBER: _ClassVar[int]
            schema: str
            table: str
            def __init__(self, schema: _Optional[str] = ..., table: _Optional[str] = ...) -> None: ...
        DATA_SAMPLING_FIELD_NUMBER: _ClassVar[int]
        TABLE_SCAN_FILTER_FIELD_NUMBER: _ClassVar[int]
        USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
        INCREMENTAL_FIELD_NUMBER: _ClassVar[int]
        data_sampling: JobTypeConfig.JobTypePiiDetect.DataSampling
        table_scan_filter: JobTypeConfig.JobTypePiiDetect.TableScanFilter
        user_prompt: str
        incremental: JobTypeConfig.JobTypePiiDetect.Incremental
        def __init__(self, data_sampling: _Optional[_Union[JobTypeConfig.JobTypePiiDetect.DataSampling, _Mapping]] = ..., table_scan_filter: _Optional[_Union[JobTypeConfig.JobTypePiiDetect.TableScanFilter, _Mapping]] = ..., user_prompt: _Optional[str] = ..., incremental: _Optional[_Union[JobTypeConfig.JobTypePiiDetect.Incremental, _Mapping]] = ...) -> None: ...
    SYNC_FIELD_NUMBER: _ClassVar[int]
    PII_DETECT_FIELD_NUMBER: _ClassVar[int]
    sync: JobTypeConfig.JobTypeSync
    pii_detect: JobTypeConfig.JobTypePiiDetect
    def __init__(self, sync: _Optional[_Union[JobTypeConfig.JobTypeSync, _Mapping]] = ..., pii_detect: _Optional[_Union[JobTypeConfig.JobTypePiiDetect, _Mapping]] = ...) -> None: ...

class WorkflowOptions(_message.Message):
    __slots__ = ("run_timeout",)
    RUN_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    run_timeout: int
    def __init__(self, run_timeout: _Optional[int] = ...) -> None: ...

class ActivityOptions(_message.Message):
    __slots__ = ("schedule_to_close_timeout", "start_to_close_timeout", "retry_policy")
    SCHEDULE_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    schedule_to_close_timeout: int
    start_to_close_timeout: int
    retry_policy: RetryPolicy
    def __init__(self, schedule_to_close_timeout: _Optional[int] = ..., start_to_close_timeout: _Optional[int] = ..., retry_policy: _Optional[_Union[RetryPolicy, _Mapping]] = ...) -> None: ...

class RetryPolicy(_message.Message):
    __slots__ = ("maximum_attempts",)
    MAXIMUM_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    maximum_attempts: int
    def __init__(self, maximum_attempts: _Optional[int] = ...) -> None: ...

class CreateJobResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: Job
    def __init__(self, job: _Optional[_Union[Job, _Mapping]] = ...) -> None: ...

class JobMappingTransformer(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _transformer_pb2.TransformerConfig
    def __init__(self, config: _Optional[_Union[_transformer_pb2.TransformerConfig, _Mapping]] = ...) -> None: ...

class JobMapping(_message.Message):
    __slots__ = ("schema", "table", "column", "transformer")
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMER_FIELD_NUMBER: _ClassVar[int]
    schema: str
    table: str
    column: str
    transformer: JobMappingTransformer
    def __init__(self, schema: _Optional[str] = ..., table: _Optional[str] = ..., column: _Optional[str] = ..., transformer: _Optional[_Union[JobMappingTransformer, _Mapping]] = ...) -> None: ...

class GetJobRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetJobResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: Job
    def __init__(self, job: _Optional[_Union[Job, _Mapping]] = ...) -> None: ...

class UpdateJobScheduleRequest(_message.Message):
    __slots__ = ("id", "cron_schedule")
    ID_FIELD_NUMBER: _ClassVar[int]
    CRON_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    id: str
    cron_schedule: str
    def __init__(self, id: _Optional[str] = ..., cron_schedule: _Optional[str] = ...) -> None: ...

class UpdateJobScheduleResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: Job
    def __init__(self, job: _Optional[_Union[Job, _Mapping]] = ...) -> None: ...

class PauseJobRequest(_message.Message):
    __slots__ = ("id", "pause", "note")
    ID_FIELD_NUMBER: _ClassVar[int]
    PAUSE_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    id: str
    pause: bool
    note: str
    def __init__(self, id: _Optional[str] = ..., pause: bool = ..., note: _Optional[str] = ...) -> None: ...

class PauseJobResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: Job
    def __init__(self, job: _Optional[_Union[Job, _Mapping]] = ...) -> None: ...

class UpdateJobSourceConnectionRequest(_message.Message):
    __slots__ = ("id", "source", "mappings", "virtual_foreign_keys", "job_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_FOREIGN_KEYS_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    source: JobSource
    mappings: _containers.RepeatedCompositeFieldContainer[JobMapping]
    virtual_foreign_keys: _containers.RepeatedCompositeFieldContainer[VirtualForeignConstraint]
    job_type: JobTypeConfig
    def __init__(self, id: _Optional[str] = ..., source: _Optional[_Union[JobSource, _Mapping]] = ..., mappings: _Optional[_Iterable[_Union[JobMapping, _Mapping]]] = ..., virtual_foreign_keys: _Optional[_Iterable[_Union[VirtualForeignConstraint, _Mapping]]] = ..., job_type: _Optional[_Union[JobTypeConfig, _Mapping]] = ...) -> None: ...

class UpdateJobSourceConnectionResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: Job
    def __init__(self, job: _Optional[_Union[Job, _Mapping]] = ...) -> None: ...

class PostgresSourceSchemaSubset(_message.Message):
    __slots__ = ("postgres_schemas",)
    POSTGRES_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    postgres_schemas: _containers.RepeatedCompositeFieldContainer[PostgresSourceSchemaOption]
    def __init__(self, postgres_schemas: _Optional[_Iterable[_Union[PostgresSourceSchemaOption, _Mapping]]] = ...) -> None: ...

class MysqlSourceSchemaSubset(_message.Message):
    __slots__ = ("mysql_schemas",)
    MYSQL_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    mysql_schemas: _containers.RepeatedCompositeFieldContainer[MysqlSourceSchemaOption]
    def __init__(self, mysql_schemas: _Optional[_Iterable[_Union[MysqlSourceSchemaOption, _Mapping]]] = ...) -> None: ...

class DynamoDBSourceSchemaSubset(_message.Message):
    __slots__ = ("tables",)
    TABLES_FIELD_NUMBER: _ClassVar[int]
    tables: _containers.RepeatedCompositeFieldContainer[DynamoDBSourceTableOption]
    def __init__(self, tables: _Optional[_Iterable[_Union[DynamoDBSourceTableOption, _Mapping]]] = ...) -> None: ...

class MssqlSourceSchemaSubset(_message.Message):
    __slots__ = ("mssql_schemas",)
    MSSQL_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    mssql_schemas: _containers.RepeatedCompositeFieldContainer[MssqlSourceSchemaOption]
    def __init__(self, mssql_schemas: _Optional[_Iterable[_Union[MssqlSourceSchemaOption, _Mapping]]] = ...) -> None: ...

class JobSourceSqlSubetSchemas(_message.Message):
    __slots__ = ("postgres_subset", "mysql_subset", "dynamodb_subset", "mssql_subset")
    POSTGRES_SUBSET_FIELD_NUMBER: _ClassVar[int]
    MYSQL_SUBSET_FIELD_NUMBER: _ClassVar[int]
    DYNAMODB_SUBSET_FIELD_NUMBER: _ClassVar[int]
    MSSQL_SUBSET_FIELD_NUMBER: _ClassVar[int]
    postgres_subset: PostgresSourceSchemaSubset
    mysql_subset: MysqlSourceSchemaSubset
    dynamodb_subset: DynamoDBSourceSchemaSubset
    mssql_subset: MssqlSourceSchemaSubset
    def __init__(self, postgres_subset: _Optional[_Union[PostgresSourceSchemaSubset, _Mapping]] = ..., mysql_subset: _Optional[_Union[MysqlSourceSchemaSubset, _Mapping]] = ..., dynamodb_subset: _Optional[_Union[DynamoDBSourceSchemaSubset, _Mapping]] = ..., mssql_subset: _Optional[_Union[MssqlSourceSchemaSubset, _Mapping]] = ...) -> None: ...

class SetJobSourceSqlConnectionSubsetsRequest(_message.Message):
    __slots__ = ("id", "schemas", "subset_by_foreign_key_constraints")
    ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    SUBSET_BY_FOREIGN_KEY_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    schemas: JobSourceSqlSubetSchemas
    subset_by_foreign_key_constraints: bool
    def __init__(self, id: _Optional[str] = ..., schemas: _Optional[_Union[JobSourceSqlSubetSchemas, _Mapping]] = ..., subset_by_foreign_key_constraints: bool = ...) -> None: ...

class SetJobSourceSqlConnectionSubsetsResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: Job
    def __init__(self, job: _Optional[_Union[Job, _Mapping]] = ...) -> None: ...

class UpdateJobDestinationConnectionRequest(_message.Message):
    __slots__ = ("job_id", "connection_id", "options", "destination_id")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    connection_id: str
    options: JobDestinationOptions
    destination_id: str
    def __init__(self, job_id: _Optional[str] = ..., connection_id: _Optional[str] = ..., options: _Optional[_Union[JobDestinationOptions, _Mapping]] = ..., destination_id: _Optional[str] = ...) -> None: ...

class UpdateJobDestinationConnectionResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: Job
    def __init__(self, job: _Optional[_Union[Job, _Mapping]] = ...) -> None: ...

class DeleteJobDestinationConnectionRequest(_message.Message):
    __slots__ = ("destination_id",)
    DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    destination_id: str
    def __init__(self, destination_id: _Optional[str] = ...) -> None: ...

class DeleteJobDestinationConnectionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateJobDestinationConnectionsRequest(_message.Message):
    __slots__ = ("job_id", "destinations")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    destinations: _containers.RepeatedCompositeFieldContainer[CreateJobDestination]
    def __init__(self, job_id: _Optional[str] = ..., destinations: _Optional[_Iterable[_Union[CreateJobDestination, _Mapping]]] = ...) -> None: ...

class CreateJobDestinationConnectionsResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: Job
    def __init__(self, job: _Optional[_Union[Job, _Mapping]] = ...) -> None: ...

class DeleteJobRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteJobResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IsJobNameAvailableRequest(_message.Message):
    __slots__ = ("name", "account_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    account_id: str
    def __init__(self, name: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class IsJobNameAvailableResponse(_message.Message):
    __slots__ = ("is_available",)
    IS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    is_available: bool
    def __init__(self, is_available: bool = ...) -> None: ...

class GetJobRunsRequest(_message.Message):
    __slots__ = ("job_id", "account_id")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    account_id: str
    def __init__(self, job_id: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class GetJobRunsResponse(_message.Message):
    __slots__ = ("job_runs",)
    JOB_RUNS_FIELD_NUMBER: _ClassVar[int]
    job_runs: _containers.RepeatedCompositeFieldContainer[JobRun]
    def __init__(self, job_runs: _Optional[_Iterable[_Union[JobRun, _Mapping]]] = ...) -> None: ...

class GetJobRunRequest(_message.Message):
    __slots__ = ("job_run_id", "account_id")
    JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    job_run_id: str
    account_id: str
    def __init__(self, job_run_id: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class GetJobRunResponse(_message.Message):
    __slots__ = ("job_run",)
    JOB_RUN_FIELD_NUMBER: _ClassVar[int]
    job_run: JobRun
    def __init__(self, job_run: _Optional[_Union[JobRun, _Mapping]] = ...) -> None: ...

class CreateJobRunRequest(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class CreateJobRunResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CancelJobRunRequest(_message.Message):
    __slots__ = ("job_run_id", "account_id")
    JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    job_run_id: str
    account_id: str
    def __init__(self, job_run_id: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class CancelJobRunResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Job(_message.Message):
    __slots__ = ("id", "created_by_user_id", "created_at", "updated_by_user_id", "updated_at", "name", "source", "destinations", "mappings", "cron_schedule", "account_id", "sync_options", "workflow_options", "virtual_foreign_keys", "job_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    CRON_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SYNC_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_FOREIGN_KEYS_FIELD_NUMBER: _ClassVar[int]
    JOB_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_by_user_id: str
    updated_at: _timestamp_pb2.Timestamp
    name: str
    source: JobSource
    destinations: _containers.RepeatedCompositeFieldContainer[JobDestination]
    mappings: _containers.RepeatedCompositeFieldContainer[JobMapping]
    cron_schedule: str
    account_id: str
    sync_options: ActivityOptions
    workflow_options: WorkflowOptions
    virtual_foreign_keys: _containers.RepeatedCompositeFieldContainer[VirtualForeignConstraint]
    job_type: JobTypeConfig
    def __init__(self, id: _Optional[str] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_by_user_id: _Optional[str] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., source: _Optional[_Union[JobSource, _Mapping]] = ..., destinations: _Optional[_Iterable[_Union[JobDestination, _Mapping]]] = ..., mappings: _Optional[_Iterable[_Union[JobMapping, _Mapping]]] = ..., cron_schedule: _Optional[str] = ..., account_id: _Optional[str] = ..., sync_options: _Optional[_Union[ActivityOptions, _Mapping]] = ..., workflow_options: _Optional[_Union[WorkflowOptions, _Mapping]] = ..., virtual_foreign_keys: _Optional[_Iterable[_Union[VirtualForeignConstraint, _Mapping]]] = ..., job_type: _Optional[_Union[JobTypeConfig, _Mapping]] = ...) -> None: ...

class JobRecentRun(_message.Message):
    __slots__ = ("start_time", "job_run_id")
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    start_time: _timestamp_pb2.Timestamp
    job_run_id: str
    def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., job_run_id: _Optional[str] = ...) -> None: ...

class GetJobRecentRunsRequest(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class GetJobRecentRunsResponse(_message.Message):
    __slots__ = ("recent_runs",)
    RECENT_RUNS_FIELD_NUMBER: _ClassVar[int]
    recent_runs: _containers.RepeatedCompositeFieldContainer[JobRecentRun]
    def __init__(self, recent_runs: _Optional[_Iterable[_Union[JobRecentRun, _Mapping]]] = ...) -> None: ...

class JobNextRuns(_message.Message):
    __slots__ = ("next_run_times",)
    NEXT_RUN_TIMES_FIELD_NUMBER: _ClassVar[int]
    next_run_times: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    def __init__(self, next_run_times: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]] = ...) -> None: ...

class GetJobNextRunsRequest(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class GetJobNextRunsResponse(_message.Message):
    __slots__ = ("next_runs",)
    NEXT_RUNS_FIELD_NUMBER: _ClassVar[int]
    next_runs: JobNextRuns
    def __init__(self, next_runs: _Optional[_Union[JobNextRuns, _Mapping]] = ...) -> None: ...

class GetJobStatusRequest(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class GetJobStatusResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: JobStatus
    def __init__(self, status: _Optional[_Union[JobStatus, str]] = ...) -> None: ...

class JobStatusRecord(_message.Message):
    __slots__ = ("job_id", "status")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    status: JobStatus
    def __init__(self, job_id: _Optional[str] = ..., status: _Optional[_Union[JobStatus, str]] = ...) -> None: ...

class GetJobStatusesRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class GetJobStatusesResponse(_message.Message):
    __slots__ = ("statuses",)
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    statuses: _containers.RepeatedCompositeFieldContainer[JobStatusRecord]
    def __init__(self, statuses: _Optional[_Iterable[_Union[JobStatusRecord, _Mapping]]] = ...) -> None: ...

class ActivityFailure(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class PendingActivity(_message.Message):
    __slots__ = ("status", "activity_name", "last_failure")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_FAILURE_FIELD_NUMBER: _ClassVar[int]
    status: ActivityStatus
    activity_name: str
    last_failure: ActivityFailure
    def __init__(self, status: _Optional[_Union[ActivityStatus, str]] = ..., activity_name: _Optional[str] = ..., last_failure: _Optional[_Union[ActivityFailure, _Mapping]] = ...) -> None: ...

class JobRun(_message.Message):
    __slots__ = ("id", "job_id", "name", "status", "started_at", "completed_at", "pending_activities")
    ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    PENDING_ACTIVITIES_FIELD_NUMBER: _ClassVar[int]
    id: str
    job_id: str
    name: str
    status: JobRunStatus
    started_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    pending_activities: _containers.RepeatedCompositeFieldContainer[PendingActivity]
    def __init__(self, id: _Optional[str] = ..., job_id: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[JobRunStatus, str]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., pending_activities: _Optional[_Iterable[_Union[PendingActivity, _Mapping]]] = ...) -> None: ...

class JobRunEventTaskError(_message.Message):
    __slots__ = ("message", "retry_state")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RETRY_STATE_FIELD_NUMBER: _ClassVar[int]
    message: str
    retry_state: str
    def __init__(self, message: _Optional[str] = ..., retry_state: _Optional[str] = ...) -> None: ...

class JobRunEventTask(_message.Message):
    __slots__ = ("id", "type", "event_time", "error")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: str
    event_time: _timestamp_pb2.Timestamp
    error: JobRunEventTaskError
    def __init__(self, id: _Optional[int] = ..., type: _Optional[str] = ..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[JobRunEventTaskError, _Mapping]] = ...) -> None: ...

class JobRunSyncMetadata(_message.Message):
    __slots__ = ("schema", "table")
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    schema: str
    table: str
    def __init__(self, schema: _Optional[str] = ..., table: _Optional[str] = ...) -> None: ...

class JobRunEventMetadata(_message.Message):
    __slots__ = ("sync_metadata",)
    SYNC_METADATA_FIELD_NUMBER: _ClassVar[int]
    sync_metadata: JobRunSyncMetadata
    def __init__(self, sync_metadata: _Optional[_Union[JobRunSyncMetadata, _Mapping]] = ...) -> None: ...

class JobRunEvent(_message.Message):
    __slots__ = ("id", "type", "start_time", "close_time", "metadata", "tasks")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    CLOSE_TIME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TASKS_FIELD_NUMBER: _ClassVar[int]
    id: int
    type: str
    start_time: _timestamp_pb2.Timestamp
    close_time: _timestamp_pb2.Timestamp
    metadata: JobRunEventMetadata
    tasks: _containers.RepeatedCompositeFieldContainer[JobRunEventTask]
    def __init__(self, id: _Optional[int] = ..., type: _Optional[str] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., close_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., metadata: _Optional[_Union[JobRunEventMetadata, _Mapping]] = ..., tasks: _Optional[_Iterable[_Union[JobRunEventTask, _Mapping]]] = ...) -> None: ...

class GetJobRunEventsRequest(_message.Message):
    __slots__ = ("job_run_id", "account_id")
    JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    job_run_id: str
    account_id: str
    def __init__(self, job_run_id: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class GetJobRunEventsResponse(_message.Message):
    __slots__ = ("events", "is_run_complete")
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    IS_RUN_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[JobRunEvent]
    is_run_complete: bool
    def __init__(self, events: _Optional[_Iterable[_Union[JobRunEvent, _Mapping]]] = ..., is_run_complete: bool = ...) -> None: ...

class DeleteJobRunRequest(_message.Message):
    __slots__ = ("job_run_id", "account_id")
    JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    job_run_id: str
    account_id: str
    def __init__(self, job_run_id: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class DeleteJobRunResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TerminateJobRunRequest(_message.Message):
    __slots__ = ("job_run_id", "account_id")
    JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    job_run_id: str
    account_id: str
    def __init__(self, job_run_id: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class TerminateJobRunResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetJobRunLogsStreamRequest(_message.Message):
    __slots__ = ("job_run_id", "account_id", "window", "should_tail", "max_log_lines", "log_levels")
    JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    SHOULD_TAIL_FIELD_NUMBER: _ClassVar[int]
    MAX_LOG_LINES_FIELD_NUMBER: _ClassVar[int]
    LOG_LEVELS_FIELD_NUMBER: _ClassVar[int]
    job_run_id: str
    account_id: str
    window: LogWindow
    should_tail: bool
    max_log_lines: int
    log_levels: _containers.RepeatedScalarFieldContainer[LogLevel]
    def __init__(self, job_run_id: _Optional[str] = ..., account_id: _Optional[str] = ..., window: _Optional[_Union[LogWindow, str]] = ..., should_tail: bool = ..., max_log_lines: _Optional[int] = ..., log_levels: _Optional[_Iterable[_Union[LogLevel, str]]] = ...) -> None: ...

class GetJobRunLogsStreamResponse(_message.Message):
    __slots__ = ("log_line", "timestamp", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    log_line: str
    timestamp: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    def __init__(self, log_line: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetJobRunLogsRequest(_message.Message):
    __slots__ = ("job_run_id", "account_id", "window", "max_log_lines", "log_levels")
    JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    WINDOW_FIELD_NUMBER: _ClassVar[int]
    MAX_LOG_LINES_FIELD_NUMBER: _ClassVar[int]
    LOG_LEVELS_FIELD_NUMBER: _ClassVar[int]
    job_run_id: str
    account_id: str
    window: LogWindow
    max_log_lines: int
    log_levels: _containers.RepeatedScalarFieldContainer[LogLevel]
    def __init__(self, job_run_id: _Optional[str] = ..., account_id: _Optional[str] = ..., window: _Optional[_Union[LogWindow, str]] = ..., max_log_lines: _Optional[int] = ..., log_levels: _Optional[_Iterable[_Union[LogLevel, str]]] = ...) -> None: ...

class GetJobRunLogsResponse(_message.Message):
    __slots__ = ("log_lines",)
    class LogLine(_message.Message):
        __slots__ = ("log_line", "timestamp", "labels")
        class LabelsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        LOG_LINE_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        log_line: str
        timestamp: _timestamp_pb2.Timestamp
        labels: _containers.ScalarMap[str, str]
        def __init__(self, log_line: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...
    LOG_LINES_FIELD_NUMBER: _ClassVar[int]
    log_lines: _containers.RepeatedCompositeFieldContainer[GetJobRunLogsResponse.LogLine]
    def __init__(self, log_lines: _Optional[_Iterable[_Union[GetJobRunLogsResponse.LogLine, _Mapping]]] = ...) -> None: ...

class SetJobWorkflowOptionsRequest(_message.Message):
    __slots__ = ("id", "worfklow_options")
    ID_FIELD_NUMBER: _ClassVar[int]
    WORFKLOW_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    worfklow_options: WorkflowOptions
    def __init__(self, id: _Optional[str] = ..., worfklow_options: _Optional[_Union[WorkflowOptions, _Mapping]] = ...) -> None: ...

class SetJobWorkflowOptionsResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: Job
    def __init__(self, job: _Optional[_Union[Job, _Mapping]] = ...) -> None: ...

class SetJobSyncOptionsRequest(_message.Message):
    __slots__ = ("id", "sync_options")
    ID_FIELD_NUMBER: _ClassVar[int]
    SYNC_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    sync_options: ActivityOptions
    def __init__(self, id: _Optional[str] = ..., sync_options: _Optional[_Union[ActivityOptions, _Mapping]] = ...) -> None: ...

class SetJobSyncOptionsResponse(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: Job
    def __init__(self, job: _Optional[_Union[Job, _Mapping]] = ...) -> None: ...

class ValidateJobMappingsRequest(_message.Message):
    __slots__ = ("account_id", "mappings", "connection_id", "virtual_foreign_keys", "job_source")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_FOREIGN_KEYS_FIELD_NUMBER: _ClassVar[int]
    JOB_SOURCE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    mappings: _containers.RepeatedCompositeFieldContainer[JobMapping]
    connection_id: str
    virtual_foreign_keys: _containers.RepeatedCompositeFieldContainer[VirtualForeignConstraint]
    job_source: JobSource
    def __init__(self, account_id: _Optional[str] = ..., mappings: _Optional[_Iterable[_Union[JobMapping, _Mapping]]] = ..., connection_id: _Optional[str] = ..., virtual_foreign_keys: _Optional[_Iterable[_Union[VirtualForeignConstraint, _Mapping]]] = ..., job_source: _Optional[_Union[JobSource, _Mapping]] = ...) -> None: ...

class ColumnError(_message.Message):
    __slots__ = ("schema", "table", "column", "errors", "error_reports")
    class ColumnErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COLUMN_ERROR_CODE_UNSPECIFIED: _ClassVar[ColumnError.ColumnErrorCode]
        COLUMN_ERROR_CODE_NOT_FOUND_IN_SOURCE: _ClassVar[ColumnError.ColumnErrorCode]
        COLUMN_ERROR_CODE_NOT_FOUND_IN_MAPPING: _ClassVar[ColumnError.ColumnErrorCode]
        COLUMN_ERROR_CODE_REQUIRED_COLUMN_NOT_FOUND_IN_MAPPING: _ClassVar[ColumnError.ColumnErrorCode]
        COLUMN_ERROR_CODE_REQUIRED_FOREIGN_KEY_NOT_FOUND_IN_MAPPING: _ClassVar[ColumnError.ColumnErrorCode]
        COLUMN_ERROR_CODE_UNSUPPORTED_CIRCULAR_DEPENDENCY_AT_LEAST_ONE_NULLABLE: _ClassVar[ColumnError.ColumnErrorCode]
        COLUMN_ERROR_CODE_VFK_SOURCE_COLUMN_NOT_FOUND_IN_MAPPING: _ClassVar[ColumnError.ColumnErrorCode]
        COLUMN_ERROR_CODE_VFK_SOURCE_COLUMN_NOT_FOUND_IN_SOURCE: _ClassVar[ColumnError.ColumnErrorCode]
        COLUMN_ERROR_CODE_VFK_TARGET_COLUMN_NOT_FOUND_IN_MAPPING: _ClassVar[ColumnError.ColumnErrorCode]
        COLUMN_ERROR_CODE_VFK_TARGET_COLUMN_NOT_FOUND_IN_SOURCE: _ClassVar[ColumnError.ColumnErrorCode]
        COLUMN_ERROR_CODE_VFK_COLUMN_DATATYPE_MISMATCH: _ClassVar[ColumnError.ColumnErrorCode]
        COLUMN_ERROR_CODE_VFK_SOURCE_COLUMN_NOT_UNIQUE: _ClassVar[ColumnError.ColumnErrorCode]
    COLUMN_ERROR_CODE_UNSPECIFIED: ColumnError.ColumnErrorCode
    COLUMN_ERROR_CODE_NOT_FOUND_IN_SOURCE: ColumnError.ColumnErrorCode
    COLUMN_ERROR_CODE_NOT_FOUND_IN_MAPPING: ColumnError.ColumnErrorCode
    COLUMN_ERROR_CODE_REQUIRED_COLUMN_NOT_FOUND_IN_MAPPING: ColumnError.ColumnErrorCode
    COLUMN_ERROR_CODE_REQUIRED_FOREIGN_KEY_NOT_FOUND_IN_MAPPING: ColumnError.ColumnErrorCode
    COLUMN_ERROR_CODE_UNSUPPORTED_CIRCULAR_DEPENDENCY_AT_LEAST_ONE_NULLABLE: ColumnError.ColumnErrorCode
    COLUMN_ERROR_CODE_VFK_SOURCE_COLUMN_NOT_FOUND_IN_MAPPING: ColumnError.ColumnErrorCode
    COLUMN_ERROR_CODE_VFK_SOURCE_COLUMN_NOT_FOUND_IN_SOURCE: ColumnError.ColumnErrorCode
    COLUMN_ERROR_CODE_VFK_TARGET_COLUMN_NOT_FOUND_IN_MAPPING: ColumnError.ColumnErrorCode
    COLUMN_ERROR_CODE_VFK_TARGET_COLUMN_NOT_FOUND_IN_SOURCE: ColumnError.ColumnErrorCode
    COLUMN_ERROR_CODE_VFK_COLUMN_DATATYPE_MISMATCH: ColumnError.ColumnErrorCode
    COLUMN_ERROR_CODE_VFK_SOURCE_COLUMN_NOT_UNIQUE: ColumnError.ColumnErrorCode
    class ColumnErrorReport(_message.Message):
        __slots__ = ("code", "message")
        CODE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        code: ColumnError.ColumnErrorCode
        message: str
        def __init__(self, code: _Optional[_Union[ColumnError.ColumnErrorCode, str]] = ..., message: _Optional[str] = ...) -> None: ...
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    ERROR_REPORTS_FIELD_NUMBER: _ClassVar[int]
    schema: str
    table: str
    column: str
    errors: _containers.RepeatedScalarFieldContainer[str]
    error_reports: _containers.RepeatedCompositeFieldContainer[ColumnError.ColumnErrorReport]
    def __init__(self, schema: _Optional[str] = ..., table: _Optional[str] = ..., column: _Optional[str] = ..., errors: _Optional[_Iterable[str]] = ..., error_reports: _Optional[_Iterable[_Union[ColumnError.ColumnErrorReport, _Mapping]]] = ...) -> None: ...

class ColumnWarning(_message.Message):
    __slots__ = ("schema", "table", "column", "warnings", "warning_reports")
    class ColumnWarningCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COLUMN_WARNING_CODE_UNSPECIFIED: _ClassVar[ColumnWarning.ColumnWarningCode]
        COLUMN_WARNING_CODE_NOT_FOUND_IN_SOURCE: _ClassVar[ColumnWarning.ColumnWarningCode]
        COLUMN_WARNING_CODE_NOT_FOUND_IN_MAPPING: _ClassVar[ColumnWarning.ColumnWarningCode]
    COLUMN_WARNING_CODE_UNSPECIFIED: ColumnWarning.ColumnWarningCode
    COLUMN_WARNING_CODE_NOT_FOUND_IN_SOURCE: ColumnWarning.ColumnWarningCode
    COLUMN_WARNING_CODE_NOT_FOUND_IN_MAPPING: ColumnWarning.ColumnWarningCode
    class ColumnWarningReport(_message.Message):
        __slots__ = ("code", "message")
        CODE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        code: ColumnWarning.ColumnWarningCode
        message: str
        def __init__(self, code: _Optional[_Union[ColumnWarning.ColumnWarningCode, str]] = ..., message: _Optional[str] = ...) -> None: ...
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    WARNING_REPORTS_FIELD_NUMBER: _ClassVar[int]
    schema: str
    table: str
    column: str
    warnings: _containers.RepeatedScalarFieldContainer[str]
    warning_reports: _containers.RepeatedCompositeFieldContainer[ColumnWarning.ColumnWarningReport]
    def __init__(self, schema: _Optional[str] = ..., table: _Optional[str] = ..., column: _Optional[str] = ..., warnings: _Optional[_Iterable[str]] = ..., warning_reports: _Optional[_Iterable[_Union[ColumnWarning.ColumnWarningReport, _Mapping]]] = ...) -> None: ...

class DatabaseError(_message.Message):
    __slots__ = ("errors", "error_reports")
    class DatabaseErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATABASE_ERROR_CODE_UNSPECIFIED: _ClassVar[DatabaseError.DatabaseErrorCode]
        DATABASE_ERROR_CODE_UNSUPPORTED_CIRCULAR_DEPENDENCY_AT_LEAST_ONE_NULLABLE: _ClassVar[DatabaseError.DatabaseErrorCode]
        DATABASE_ERROR_CODE_VFK_COLUMN_MISMATCH: _ClassVar[DatabaseError.DatabaseErrorCode]
    DATABASE_ERROR_CODE_UNSPECIFIED: DatabaseError.DatabaseErrorCode
    DATABASE_ERROR_CODE_UNSUPPORTED_CIRCULAR_DEPENDENCY_AT_LEAST_ONE_NULLABLE: DatabaseError.DatabaseErrorCode
    DATABASE_ERROR_CODE_VFK_COLUMN_MISMATCH: DatabaseError.DatabaseErrorCode
    class DatabaseErrorReport(_message.Message):
        __slots__ = ("code", "message")
        CODE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        code: DatabaseError.DatabaseErrorCode
        message: str
        def __init__(self, code: _Optional[_Union[DatabaseError.DatabaseErrorCode, str]] = ..., message: _Optional[str] = ...) -> None: ...
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    ERROR_REPORTS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedScalarFieldContainer[str]
    error_reports: _containers.RepeatedCompositeFieldContainer[DatabaseError.DatabaseErrorReport]
    def __init__(self, errors: _Optional[_Iterable[str]] = ..., error_reports: _Optional[_Iterable[_Union[DatabaseError.DatabaseErrorReport, _Mapping]]] = ...) -> None: ...

class TableError(_message.Message):
    __slots__ = ("schema", "table", "error_reports")
    class TableErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TABLE_ERROR_CODE_UNSPECIFIED: _ClassVar[TableError.TableErrorCode]
        TABLE_ERROR_CODE_TABLE_NOT_FOUND_IN_SOURCE: _ClassVar[TableError.TableErrorCode]
        TABLE_ERROR_CODE_VFK_SOURCE_TABLE_NOT_FOUND_IN_MAPPING: _ClassVar[TableError.TableErrorCode]
        TABLE_ERROR_CODE_VFK_SOURCE_TABLE_NOT_FOUND_IN_SOURCE: _ClassVar[TableError.TableErrorCode]
        TABLE_ERROR_CODE_VFK_TARGET_TABLE_NOT_FOUND_IN_MAPPING: _ClassVar[TableError.TableErrorCode]
        TABLE_ERROR_CODE_VFK_TARGET_TABLE_NOT_FOUND_IN_SOURCE: _ClassVar[TableError.TableErrorCode]
    TABLE_ERROR_CODE_UNSPECIFIED: TableError.TableErrorCode
    TABLE_ERROR_CODE_TABLE_NOT_FOUND_IN_SOURCE: TableError.TableErrorCode
    TABLE_ERROR_CODE_VFK_SOURCE_TABLE_NOT_FOUND_IN_MAPPING: TableError.TableErrorCode
    TABLE_ERROR_CODE_VFK_SOURCE_TABLE_NOT_FOUND_IN_SOURCE: TableError.TableErrorCode
    TABLE_ERROR_CODE_VFK_TARGET_TABLE_NOT_FOUND_IN_MAPPING: TableError.TableErrorCode
    TABLE_ERROR_CODE_VFK_TARGET_TABLE_NOT_FOUND_IN_SOURCE: TableError.TableErrorCode
    class TableErrorReport(_message.Message):
        __slots__ = ("code", "message")
        CODE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        code: TableError.TableErrorCode
        message: str
        def __init__(self, code: _Optional[_Union[TableError.TableErrorCode, str]] = ..., message: _Optional[str] = ...) -> None: ...
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_REPORTS_FIELD_NUMBER: _ClassVar[int]
    schema: str
    table: str
    error_reports: _containers.RepeatedCompositeFieldContainer[TableError.TableErrorReport]
    def __init__(self, schema: _Optional[str] = ..., table: _Optional[str] = ..., error_reports: _Optional[_Iterable[_Union[TableError.TableErrorReport, _Mapping]]] = ...) -> None: ...

class ValidateJobMappingsResponse(_message.Message):
    __slots__ = ("column_errors", "database_errors", "column_warnings", "table_errors")
    COLUMN_ERRORS_FIELD_NUMBER: _ClassVar[int]
    DATABASE_ERRORS_FIELD_NUMBER: _ClassVar[int]
    COLUMN_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    TABLE_ERRORS_FIELD_NUMBER: _ClassVar[int]
    column_errors: _containers.RepeatedCompositeFieldContainer[ColumnError]
    database_errors: DatabaseError
    column_warnings: _containers.RepeatedCompositeFieldContainer[ColumnWarning]
    table_errors: _containers.RepeatedCompositeFieldContainer[TableError]
    def __init__(self, column_errors: _Optional[_Iterable[_Union[ColumnError, _Mapping]]] = ..., database_errors: _Optional[_Union[DatabaseError, _Mapping]] = ..., column_warnings: _Optional[_Iterable[_Union[ColumnWarning, _Mapping]]] = ..., table_errors: _Optional[_Iterable[_Union[TableError, _Mapping]]] = ...) -> None: ...

class ValidateSchemaRequest(_message.Message):
    __slots__ = ("mappings", "connection_id")
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
    mappings: _containers.RepeatedCompositeFieldContainer[JobMapping]
    connection_id: str
    def __init__(self, mappings: _Optional[_Iterable[_Union[JobMapping, _Mapping]]] = ..., connection_id: _Optional[str] = ...) -> None: ...

class ValidateSchemaResponse(_message.Message):
    __slots__ = ("missing_columns", "extra_columns", "missing_tables", "missing_schemas")
    class Table(_message.Message):
        __slots__ = ("schema", "table")
        SCHEMA_FIELD_NUMBER: _ClassVar[int]
        TABLE_FIELD_NUMBER: _ClassVar[int]
        schema: str
        table: str
        def __init__(self, schema: _Optional[str] = ..., table: _Optional[str] = ...) -> None: ...
    MISSING_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_COLUMNS_FIELD_NUMBER: _ClassVar[int]
    MISSING_TABLES_FIELD_NUMBER: _ClassVar[int]
    MISSING_SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    missing_columns: _containers.RepeatedCompositeFieldContainer[_connection_data_pb2.DatabaseColumn]
    extra_columns: _containers.RepeatedCompositeFieldContainer[_connection_data_pb2.DatabaseColumn]
    missing_tables: _containers.RepeatedCompositeFieldContainer[ValidateSchemaResponse.Table]
    missing_schemas: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, missing_columns: _Optional[_Iterable[_Union[_connection_data_pb2.DatabaseColumn, _Mapping]]] = ..., extra_columns: _Optional[_Iterable[_Union[_connection_data_pb2.DatabaseColumn, _Mapping]]] = ..., missing_tables: _Optional[_Iterable[_Union[ValidateSchemaResponse.Table, _Mapping]]] = ..., missing_schemas: _Optional[_Iterable[str]] = ...) -> None: ...

class VirtualForeignKey(_message.Message):
    __slots__ = ("schema", "table", "columns")
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    schema: str
    table: str
    columns: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, schema: _Optional[str] = ..., table: _Optional[str] = ..., columns: _Optional[_Iterable[str]] = ...) -> None: ...

class VirtualForeignConstraint(_message.Message):
    __slots__ = ("schema", "table", "columns", "foreign_key")
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    FOREIGN_KEY_FIELD_NUMBER: _ClassVar[int]
    schema: str
    table: str
    columns: _containers.RepeatedScalarFieldContainer[str]
    foreign_key: VirtualForeignKey
    def __init__(self, schema: _Optional[str] = ..., table: _Optional[str] = ..., columns: _Optional[_Iterable[str]] = ..., foreign_key: _Optional[_Union[VirtualForeignKey, _Mapping]] = ...) -> None: ...

class RunContextKey(_message.Message):
    __slots__ = ("job_run_id", "external_id", "account_id")
    JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    job_run_id: str
    external_id: str
    account_id: str
    def __init__(self, job_run_id: _Optional[str] = ..., external_id: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class GetRunContextRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: RunContextKey
    def __init__(self, id: _Optional[_Union[RunContextKey, _Mapping]] = ...) -> None: ...

class GetRunContextResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    def __init__(self, value: _Optional[bytes] = ...) -> None: ...

class SetRunContextRequest(_message.Message):
    __slots__ = ("id", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: RunContextKey
    value: bytes
    def __init__(self, id: _Optional[_Union[RunContextKey, _Mapping]] = ..., value: _Optional[bytes] = ...) -> None: ...

class SetRunContextResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetRunContextsRequest(_message.Message):
    __slots__ = ("id", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: RunContextKey
    value: bytes
    def __init__(self, id: _Optional[_Union[RunContextKey, _Mapping]] = ..., value: _Optional[bytes] = ...) -> None: ...

class SetRunContextsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JobHook(_message.Message):
    __slots__ = ("id", "name", "description", "job_id", "config", "created_by_user_id", "created_at", "updated_by_user_id", "updated_at", "enabled", "priority")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    job_id: str
    config: JobHookConfig
    created_by_user_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_by_user_id: str
    updated_at: _timestamp_pb2.Timestamp
    enabled: bool
    priority: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., job_id: _Optional[str] = ..., config: _Optional[_Union[JobHookConfig, _Mapping]] = ..., created_by_user_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_by_user_id: _Optional[str] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., enabled: bool = ..., priority: _Optional[int] = ...) -> None: ...

class NewJobHook(_message.Message):
    __slots__ = ("name", "description", "config", "enabled", "priority")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    config: JobHookConfig
    enabled: bool
    priority: int
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., config: _Optional[_Union[JobHookConfig, _Mapping]] = ..., enabled: bool = ..., priority: _Optional[int] = ...) -> None: ...

class JobHookConfig(_message.Message):
    __slots__ = ("sql",)
    class JobSqlHook(_message.Message):
        __slots__ = ("query", "connection_id", "timing")
        class Timing(_message.Message):
            __slots__ = ("pre_sync", "post_sync")
            PRE_SYNC_FIELD_NUMBER: _ClassVar[int]
            POST_SYNC_FIELD_NUMBER: _ClassVar[int]
            pre_sync: JobHookTimingPreSync
            post_sync: JobHookTimingPostSync
            def __init__(self, pre_sync: _Optional[_Union[JobHookTimingPreSync, _Mapping]] = ..., post_sync: _Optional[_Union[JobHookTimingPostSync, _Mapping]] = ...) -> None: ...
        QUERY_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
        TIMING_FIELD_NUMBER: _ClassVar[int]
        query: str
        connection_id: str
        timing: JobHookConfig.JobSqlHook.Timing
        def __init__(self, query: _Optional[str] = ..., connection_id: _Optional[str] = ..., timing: _Optional[_Union[JobHookConfig.JobSqlHook.Timing, _Mapping]] = ...) -> None: ...
    SQL_FIELD_NUMBER: _ClassVar[int]
    sql: JobHookConfig.JobSqlHook
    def __init__(self, sql: _Optional[_Union[JobHookConfig.JobSqlHook, _Mapping]] = ...) -> None: ...

class JobHookTimingPreSync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class JobHookTimingPostSync(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetJobHooksRequest(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class GetJobHooksResponse(_message.Message):
    __slots__ = ("hooks",)
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    hooks: _containers.RepeatedCompositeFieldContainer[JobHook]
    def __init__(self, hooks: _Optional[_Iterable[_Union[JobHook, _Mapping]]] = ...) -> None: ...

class GetJobHookRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetJobHookResponse(_message.Message):
    __slots__ = ("hook",)
    HOOK_FIELD_NUMBER: _ClassVar[int]
    hook: JobHook
    def __init__(self, hook: _Optional[_Union[JobHook, _Mapping]] = ...) -> None: ...

class CreateJobHookRequest(_message.Message):
    __slots__ = ("job_id", "hook")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    HOOK_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    hook: NewJobHook
    def __init__(self, job_id: _Optional[str] = ..., hook: _Optional[_Union[NewJobHook, _Mapping]] = ...) -> None: ...

class CreateJobHookResponse(_message.Message):
    __slots__ = ("hook",)
    HOOK_FIELD_NUMBER: _ClassVar[int]
    hook: JobHook
    def __init__(self, hook: _Optional[_Union[JobHook, _Mapping]] = ...) -> None: ...

class DeleteJobHookRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteJobHookResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IsJobHookNameAvailableRequest(_message.Message):
    __slots__ = ("job_id", "name")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    name: str
    def __init__(self, job_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class IsJobHookNameAvailableResponse(_message.Message):
    __slots__ = ("is_available",)
    IS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    is_available: bool
    def __init__(self, is_available: bool = ...) -> None: ...

class UpdateJobHookRequest(_message.Message):
    __slots__ = ("id", "name", "description", "config", "enabled", "priority")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    config: JobHookConfig
    enabled: bool
    priority: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., config: _Optional[_Union[JobHookConfig, _Mapping]] = ..., enabled: bool = ..., priority: _Optional[int] = ...) -> None: ...

class UpdateJobHookResponse(_message.Message):
    __slots__ = ("hook",)
    HOOK_FIELD_NUMBER: _ClassVar[int]
    hook: JobHook
    def __init__(self, hook: _Optional[_Union[JobHook, _Mapping]] = ...) -> None: ...

class SetJobHookEnabledRequest(_message.Message):
    __slots__ = ("id", "enabled")
    ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: str
    enabled: bool
    def __init__(self, id: _Optional[str] = ..., enabled: bool = ...) -> None: ...

class SetJobHookEnabledResponse(_message.Message):
    __slots__ = ("hook",)
    HOOK_FIELD_NUMBER: _ClassVar[int]
    hook: JobHook
    def __init__(self, hook: _Optional[_Union[JobHook, _Mapping]] = ...) -> None: ...

class GetActiveJobHooksByTimingRequest(_message.Message):
    __slots__ = ("job_id", "timing")
    class Timing(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIMING_UNSPECIFIED: _ClassVar[GetActiveJobHooksByTimingRequest.Timing]
        TIMING_PRESYNC: _ClassVar[GetActiveJobHooksByTimingRequest.Timing]
        TIMING_POSTSYNC: _ClassVar[GetActiveJobHooksByTimingRequest.Timing]
    TIMING_UNSPECIFIED: GetActiveJobHooksByTimingRequest.Timing
    TIMING_PRESYNC: GetActiveJobHooksByTimingRequest.Timing
    TIMING_POSTSYNC: GetActiveJobHooksByTimingRequest.Timing
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    timing: GetActiveJobHooksByTimingRequest.Timing
    def __init__(self, job_id: _Optional[str] = ..., timing: _Optional[_Union[GetActiveJobHooksByTimingRequest.Timing, str]] = ...) -> None: ...

class GetActiveJobHooksByTimingResponse(_message.Message):
    __slots__ = ("hooks",)
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    hooks: _containers.RepeatedCompositeFieldContainer[JobHook]
    def __init__(self, hooks: _Optional[_Iterable[_Union[JobHook, _Mapping]]] = ...) -> None: ...

class GetPiiDetectionReportRequest(_message.Message):
    __slots__ = ("job_run_id", "account_id")
    JOB_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    job_run_id: str
    account_id: str
    def __init__(self, job_run_id: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class GetPiiDetectionReportResponse(_message.Message):
    __slots__ = ("report",)
    REPORT_FIELD_NUMBER: _ClassVar[int]
    report: PiiDetectionReport
    def __init__(self, report: _Optional[_Union[PiiDetectionReport, _Mapping]] = ...) -> None: ...

class PiiDetectionReport(_message.Message):
    __slots__ = ("tables",)
    class TableReport(_message.Message):
        __slots__ = ("schema", "table", "columns")
        class ColumnReport(_message.Message):
            __slots__ = ("column", "regex_report", "llm_report")
            class Regex(_message.Message):
                __slots__ = ("category",)
                CATEGORY_FIELD_NUMBER: _ClassVar[int]
                category: str
                def __init__(self, category: _Optional[str] = ...) -> None: ...
            class LLM(_message.Message):
                __slots__ = ("category", "confidence")
                CATEGORY_FIELD_NUMBER: _ClassVar[int]
                CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
                category: str
                confidence: float
                def __init__(self, category: _Optional[str] = ..., confidence: _Optional[float] = ...) -> None: ...
            COLUMN_FIELD_NUMBER: _ClassVar[int]
            REGEX_REPORT_FIELD_NUMBER: _ClassVar[int]
            LLM_REPORT_FIELD_NUMBER: _ClassVar[int]
            column: str
            regex_report: PiiDetectionReport.TableReport.ColumnReport.Regex
            llm_report: PiiDetectionReport.TableReport.ColumnReport.LLM
            def __init__(self, column: _Optional[str] = ..., regex_report: _Optional[_Union[PiiDetectionReport.TableReport.ColumnReport.Regex, _Mapping]] = ..., llm_report: _Optional[_Union[PiiDetectionReport.TableReport.ColumnReport.LLM, _Mapping]] = ...) -> None: ...
        SCHEMA_FIELD_NUMBER: _ClassVar[int]
        TABLE_FIELD_NUMBER: _ClassVar[int]
        COLUMNS_FIELD_NUMBER: _ClassVar[int]
        schema: str
        table: str
        columns: _containers.RepeatedCompositeFieldContainer[PiiDetectionReport.TableReport.ColumnReport]
        def __init__(self, schema: _Optional[str] = ..., table: _Optional[str] = ..., columns: _Optional[_Iterable[_Union[PiiDetectionReport.TableReport.ColumnReport, _Mapping]]] = ...) -> None: ...
    TABLES_FIELD_NUMBER: _ClassVar[int]
    tables: _containers.RepeatedCompositeFieldContainer[PiiDetectionReport.TableReport]
    def __init__(self, tables: _Optional[_Iterable[_Union[PiiDetectionReport.TableReport, _Mapping]]] = ...) -> None: ...
