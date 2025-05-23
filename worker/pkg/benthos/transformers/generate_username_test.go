package transformers

import (
	"fmt"
	"testing"
	"time"

	"github.com/nucleuscloud/neosync/worker/pkg/rng"
	"github.com/redpanda-data/benthos/v4/public/bloblang"
	"github.com/stretchr/testify/assert"
)

func Test_GenerateUsername(t *testing.T) {
	randomizer := rng.New(2)
	res, err := generateUsername(randomizer, maxLength)
	assert.NoError(t, err)

	assert.IsType(t, "", res, "The expected username should have a valid username")
	assert.LessOrEqual(t, int64(len(res)), maxLength, fmt.Sprintf("The city should be less than or equal to the max length. This is the error city:%s", res))
}

func Test_GenerateUsername_Random_Seed(t *testing.T) {
	seed := time.Now().UnixNano()
	randomizer := rng.New(seed)
	res, err := generateUsername(randomizer, maxLength)
	assert.NoError(t, err, "failed with seed", "seed", seed)

	assert.IsType(t, "", res, "The expected username should have a valid username")
	assert.LessOrEqual(t, int64(len(res)), maxLength, fmt.Sprintf("The city should be less than or equal to the max length. This is the error city:%s", res))
}

func Test_GenerateUsernameShort(t *testing.T) {
	randomizer := rng.New(1)
	res, err := generateUsername(randomizer, 3)
	assert.NoError(t, err)

	assert.IsType(t, "", res, "The expected username should have a valid username")
	assert.LessOrEqual(t, int64(len(res)), int64(3), fmt.Sprintf("The city should be less than or equal to the max length. This is the error city:%s", res))
}

func Test_UsernamelTransformer(t *testing.T) {
	mapping := fmt.Sprintf(`root = generate_username(max_length: %d)`, maxLength)
	ex, err := bloblang.Parse(mapping)

	assert.NoError(t, err, "failed to parse the realistic username transformer")

	res, err := ex.Query(nil)
	assert.NoError(t, err)

	assert.IsType(t, "", res, "The expected username should have a valid username")
}

func Test_UsernamelTransformer_NoOptions(t *testing.T) {
	mapping := `root = generate_username()`
	ex, err := bloblang.Parse(mapping)

	assert.NoError(t, err, "failed to parse the realistic username transformer")

	res, err := ex.Query(nil)
	assert.NoError(t, err)
	assert.NotEmpty(t, res)
}
