# 救救我的統計 R 桌面版

目前版號：`1.0.0`

## 本機開發

```bash
npm ci
npm run desktop
```

## 產生目前作業系統的安裝檔

```bash
npm run version:check
npm run desktop:bundle
```

輸出位於 `src-tauri/target/release/bundle/`。桌面版會把完整課程與圖片嵌入程式，不需要網站 server 或網路連線。

## 發布新版

1. 同步修改 `package.json`、`src-tauri/tauri.conf.json`、`src-tauri/Cargo.toml` 的版號。
2. 執行 `npm run version:check` 與 `npm test`。
3. 提交後建立並推送標籤，例如：

```bash
git tag desktop-v1.0.0
git push origin desktop-v1.0.0
```

GitHub Actions 會建立 Release，並附上 macOS、Windows 與 Linux 的安裝檔。未設定 Apple／Windows 正式簽章前，下載者可能會看到作業系統的安全警告。
