涵蓋了從課程介紹、環境設定、作業繳交到與老師的課程內容保持同步的全部流程
-----

# 地球物理學程式設計 - 2025 課程專案

歡迎來到 `geophysics-class-2025` 課程！ 👋

本課程的所有程式設計作業與實驗，都將在 **GitHub Codespaces** 這個強大的雲端開發環境中進行。你只需要一個網頁瀏覽器，就可以開始學習，完全不用在自己的電腦上安裝任何複雜的軟體！

# 為了載入環境變數，剛進入codespace時請執行 ： source env.sh
# 為了push更新到自己的repo，請執行 ： sh git_all.sh "comments"

## 🚀 為什麼我們使用 GitHub Codespaces？

  * 💻 **免安裝，零設定**：你不需要在自己的電腦上安裝 Python、Conda、ObsPy、PyGMT 等任何工具。所有需要的軟體都已經在雲端準備好了。
  * 🌐 **環境完全一致**：告別「老師的電腦可以跑，我的電腦卻出錯」的惡夢！每個人使用的都是完全相同的環境，確保程式碼的執行結果一致。
  * ✍️ **整合專業級編輯器**：直接在瀏覽器中使用功能強大的 VS Code 編輯器，無論是寫 Python 程式碼、操作 Jupyter Notebook 還是下達終端機指令，都非常流暢。
  * 🤝 **即時協作與問答**：當你遇到問題時，老師或助教可以透過一個連結直接進入你的 Codespace 環境，即時幫你找出問題並進行指導。

## 📁 專案結構

這個 Repository (簡稱 Repo) 包含了課程所需的所有資源：

  * `/.devcontainer/`：定義 Codespaces 雲端環境的設定檔，你不需要修改它。
  * `/data/`：存放課程中會用到的地震資料、CSV 檔等。
  * `/notebooks/`：存放 Jupyter Notebook 範例程式碼與課程講義。
  * `/hw/`：各週的作業說明與需要你完成的檔案。

-----

## 📝 作業與課程完整工作流程

請遵循以下步驟來設定環境、同步課程、完成並繳交作業。這套流程是軟體開發的業界標準，學會它將對你非常有幫助！

### 第 1 步：Fork 課程專案到你的帳號 (一學期一次)

「Fork」的意思是將老師的課程 Repo 完整地複製一份到你自己的 GitHub 帳號下，變成你個人的專屬副本。**這是整個學期你只需要做一次的動作。**

1.  前往本課程的 GitHub Repo：[https://github.com/cwbdayi638/geophysics-class-2025](https://github.com/cwbdayi638/geophysics-class-2025)
2.  點擊頁面右上角的 **Fork** 按鈕。
3.  在跳出的頁面中，直接點擊 **Create fork**。

完成後，你的帳號下就會有一個一模一樣的 Repo。之後的所有作業與操作，你都會在**你自己的這個副本**中完成。

### 第 2 步：建立你的雲端開發環境 (Codespace)

**每次要開始做作業或實驗時，請執行這個步驟。**

1.  進入你**自己帳號下** Fork 好的 Repo。
2.  點擊頁面中綠色的 **`< > Code`** 按鈕。
3.  選擇 **Create codespace on main**。
4.  請耐心等待約 1-2 分鐘，Codespaces 會在背景自動幫你安裝好所有需要的軟體。完成後，你就會看到一個完整的 VS Code 開發介面。

-----

### 第 3 步：同步老師的更新 (獲取最新教材與作業)

在開始做新作業前，你應該先將老師主專案的最新變動同步到你的專案中。

#### A. 設定上游 Repository (只需設定一次)

你需要告訴 Git 老師的原始 Repo 在哪裡。我們稱之為 `upstream` (上游)。

1.  在 Codespace 終端機中，貼上以下指令：
    ```bash
    git remote add upstream https://github.com/cwbdayi638/geophysics-class-2025.git
    ```
2.  執行 `git remote -v` 確認 `upstream` 已成功新增。

#### B. 拉取與同步更新 (日常操作)

> **⚠️ 操作前請注意：**
> 在同步之前，請先確認你自己的作業修改都已經 `commit`。你可以使用 `git status` 來檢查。

1.  **從 `upstream` (老師的 Repo) 拉取最新的變更**。
    ```bash
    git fetch upstream
    ```
2.  **將 `upstream` 的 `main` 分支合併 (Merge) 到你自己的 `main` 分支**。
    ```bash
    git merge upstream/main
    ```
3.  **將同步後的版本推送到你自己的 GitHub Fork Repo (`origin`)**。
    ```bash
    git push origin main
    ```

完成後，你就可以在左側的檔案總管看到老師新增的作業或教材了。

-----

### 第 4 步：在 Codespace 中完成作業並儲存進度

1.  在左側的檔案總管中，找到當週的作業資料夾（例如 `/hw/hw1/`）並開始寫作業，作業檔名為：”學號.ipynb“。

2.  完成作業的一部分或全部時，你需要將變更「儲存」回你 Fork 的 Repo。請在**終端機**執行以下指令：

    ```bash
    # 1. 加入所有變更
    git add .

    # 2. 建立版本紀錄 (請修改 "" 中的文字為有意義的描述)
    git commit -m "完成 HW1 第一、二題"

    # 3. 推送到你的 GitHub Repo
    git push
    ```

### 第 5 步：繳交作業 (建立 Pull Request)

**每份作業只需要繳交一次。**

當你確定作業完成並已 `push` 所有進度後，就可以正式繳交了。繳交的方式是建立一個 "Pull Request" (簡稱 PR)。

1.  回到你 GitHub 上 Fork 的 Repo 頁面。
2.  你會看到一個提示 "This branch is ... ahead of..."，點擊右側的 **Contribute** -\> **Open pull request**。
3.  **確認標題與內容**：
      * **標題 (Title)**：請填寫有意義的標題，例如 `[HW1] 姓名 - 學號`。
      * **內容 (Leave a comment)**：這是作業最重要的部分！請在這裡詳細說明你的**作業目的、方法、附上結果圖、你的觀察與討論**。
4.  確認 Base Repository 是老師的 Repo (`cwbdayi638/geophysics-class-2025`)，而 Head Repository 是你自己的 Repo。
5.  點擊 **Create pull request**，作業就成功繳交了！

### 第 6 步：接收老師的回饋與修改

老師會在你的 Pull Request 頁面中直接留言給你評語、分數，或要求修改。如果需要修改，你只需要回到你的 Codespace 環境，修改程式碼，然後再次執行 `git add`, `git commit`, `git push`。你新的 `push` 會**自動更新**到已經開啟的 Pull Request 中，不需要重新建立一個新的 PR。

-----

## ❓ 常見問題：如果發生「合併衝突 (Merge Conflict)」怎麼辦？

如果你修改了某個檔案，而老師也剛好修改了**同一個檔案的同一行**，在 `git merge` 時就會發生「衝突」。

  * **不要慌張**：這是 Git 的正常機制。
  * **查看檔案**：VS Code 會高亮顯示衝突的檔案。打開它，你會看到類似 `<<<<<<<`、`=======`、`>>>>>>>` 的標記。
  * **手動解決**：VS Code 會提供視覺化介面讓你選擇要保留「你的修改 (Incoming Change)」還是「老師的修改 (Current Change)」，或者兩者都保留。請根據情況手動編輯檔案，直到內容是你想要的樣子，並刪除所有衝突標記。
  * **完成合併**：解決衝突後，儲存檔案，然後執行 `git add .` 和 `git commit` 來完成這次合併。
  * **尋求協助**：如果對解決衝突沒有把握，請立即向老師或助教求助！

祝學習愉快！
