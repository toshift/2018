# Powershell有効コマンド
# Set-ExecutionPolicy RemoteSigned 

# 今日のプログラミング用のディレクトリを作成する

### 共通データ定義
#[String[]]$PATH = C:\work\github\2018
# Set-Locationにパラメータを渡したかったのに渡せなかったので、方法を探し中。

function MakeDir($name) {
    if ((Test-Path $name) -eq $False ){
        New-Item -ItemType Directory -Path $name
        return
    }
}

function Main {
    $gitpath = "C:\work\github\2018"
    # gitのpathに変更する
    Set-Location $gitpath
    $dir_name = (Get-Date).ToString("MMdd")
    MakeDir($dir_name)
}

Main;