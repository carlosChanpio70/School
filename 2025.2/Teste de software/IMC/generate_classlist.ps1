Get-ChildItem -Path 'target\classes' -Recurse -Filter *.class | ForEach-Object {
    $p = $_.FullName
    $n = $p -replace '^.*?target\\classes\\','' -replace '\\','.' -replace '\.class$',''
    Write-Output $n
}