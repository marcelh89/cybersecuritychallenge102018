$path = "d:\archives"
$7zip = "C:\Program Files\7-Zip\7z.exe"
$items = Get-ChildItem -Path $path
 
foreach ($item in $items)
{
      if ($item.Attributes -eq "Directory")
      {
        Write-Host $item.Name
        cd "$path\$item"
        & $7zip x $path\$item\*.bz2
      }
}