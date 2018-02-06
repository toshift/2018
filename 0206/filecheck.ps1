function Main {
    $a = Get-ChildItem | Select-Object -Property Name
    Write-Host $a
}
Main