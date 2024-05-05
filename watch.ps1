pushd $PSScriptRoot

# Set up 0repo
if ((Split-Path $(pwd) -Leaf) -ne "feeds") {
  throw "This Git repo must be cloned into a directory named 'feeds' in order for 0repo to work."
}
if (!(Test-Path ..\0repo-config.py)) {copy 0repo-config.py.template ..\0repo-config.py}
mkdir -Force ..\incoming | Out-Null
copy *\*.zip ..\incoming\

# Run watch scripts
$files = (ls -Recurse -Filter *.watch.py .).FullName
foreach ($file in $files) {
    echo "Running $file"
    cmd /c "0install run --batch https://apps.0install.net/0install/0watch.xml --output ..\incoming $file 2>&1" # Redirect stderr to stdout
    if ($LASTEXITCODE -ne 0) {throw "Failed with exit code $LASTEXITCODE"}
}

# Merge generated feeds
cd ..
cmd /c "0install run https://apps.0install.net/0install/0repo.xml 2>&1" # Ignore error due to missing archives.db

popd
