## セクション3で学んだことメモ
### JSONとは？
* JavaSrcript Object Notationの略
  * JavaScriptのオブジェクトの表記方法をもとにしたデータフォーマット（Python辞書と同じ）
    * キーは必ずダブルクォーテーションで囲む必要あり
```
{
  "id": "1",
  "name": "taro"
}
```

### Web APIとは？
* HTTP/HTTPSベースで実現するAPI、Webを介して使用するAPI

### RESTful API（REST API）とは？
* REpresentational State Transferの略、APIで用いられるルール
* 4つの原則から成り立つAPIで用いられる
  * アドレス可能性
    * すべての情報が一意なURI（1つのURIですべての機能を表現できる）
    　 * URIの中の一部としてURLがある
  * ステートレス性
    * すべてのリクエストが完全に分離し、セクションなどの状態管理は行われない
  * 接続性
    * 別の情報へのリンクを含めること
  * 統一インターフェース
    * 情報の取得、作成、更新、削除の操作をHTTPメソッドを利用
      * POST：データを新規作成
      * GET：データを取得
      * PUT：データを更新
      * DELETE：データを削除