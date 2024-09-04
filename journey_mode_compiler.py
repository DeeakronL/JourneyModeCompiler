inputLines = open("input.txt")
inputConfig = open("compiler_config.txt")
lines = []
config = []
output = []

for line in inputLines:
	lines.append(line)

for line in inputConfig:
	config.append(line)

stackNum = int(config[1].strip("\n"))

output.append("{\n")
output.append("  \"category\": \"Changes\",\n")
output.append("  \"items\": [\n")
i = 0
while i < len(lines):
	if i > 0:
		output.append("    },\n")
	output.append("    {\n")
	output.append("      \"item\": \"" + lines[i].strip("\n") + "\",\n")
	output.append("      \"count\": " + str(stackNum) + ",\n")
	output.append("      \"category\": \"Modded Items\"\n")
	i += 1

output.append("    }\n")
output.append("  ]\n")
output.append("}")

outputResult = open("changes.json", "w")
for j in output:
	outputResult.write(j)
outputResult.close()