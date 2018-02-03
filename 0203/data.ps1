# 参考 http://powershell.wiki.fc2.com/wiki/HDD%E3%81%AE%E4%BD%BF%E7%94%A8%E9%87%8F%E3%82%92%E7%A2%BA%E8%AA%8D%E3%81%99%E3%82%8B
function dataview {
    Param([String]$computerName=".")

    $disks = Get-WmiObject Win32_LogicalDisk -ComputerName $computerName `
      | ?{$_.DriveType -eq 3}

    foreach ($disk in $disks) {
        Write-Host ドライブレター:    $disk.DeviceID
        Write-Host 容量 :("{0,6:0.00}" -F ($disk.Size / 1GB))GB
        Write-Host 空き容量: ("{0,6:0.00}" -F ($disk.FreeSpace / 1GB)) GB
        $used = [Decimal]$disk.Size - [Decimal]$disk.FreeSpace 
        Write-Host 使用量:("{0,6:0.00}" -F ($used / 1GB))GB
        Write-Host
    }
}

function Main{
    dataview 
    Start-Sleep 5
}

Main
