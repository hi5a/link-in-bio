# SPDX-FileCopyrightText: Andrew Ball <andrew@aball.dev>
npm run trueBuild
SHORT_COMMIT=$(git rev-parse --short HEAD)
LONG_COMMIT=$(git rev-parse HEAD)
echo "Building project from $SHORT_COMMIT"

sed -i "s/{{SHORT_COMMIT}}/$SHORT_COMMIT/g" ./dist/index.html
sed -i "s/{{LONG_COMMIT}}/$LONG_COMMIT/g" ./dist/index.html