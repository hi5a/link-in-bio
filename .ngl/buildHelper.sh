npm run trueBuild
SHORT_COMMIT=$(git rev-parse --short HEAD)
LONG_COMMIT=$(git rev-parse HEAD)

sed -i "s/{{SHORT_COMMIT}}/$SHORT_COMMIT/g" ./dist/index.html
sed -i "s/{{LONG_COMMIT}}/$LONG_COMMIT/g" ./dist/index.html