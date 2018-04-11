$ErrorActionPreference = "Stop"
pushd $(Split-Path -Path $MyInvocation.MyCommand.Definition -Parent)

# Ensure 0install is in the PATH
if (!(Get-Command 0install -ErrorAction SilentlyContinue)) {
    mkdir -Force "$env:TEMP\zero-install" | Out-Null
    Invoke-WebRequest "https://0install.de/files/0install.exe" -OutFile "$env:TEMP\zero-install\0install.exe"
    $env:PATH = "$env:TEMP\zero-install;$env:PATH"
}

if (!(Test-Path incoming)) { mkdir incoming | Out-Null }

foreach ($file in (ls -Recurse -Filter *.watch.py .).FullName) {
    echo "Checking $file"
    cmd /c "0install run --batch http://0install.de/feeds/0watch.xml --output incoming $file 2>&1" # Redirect stderr to stdout
    if ($LASTEXITCODE -ne 0) {throw "Exit Code: $LASTEXITCODE"}
}

popd
