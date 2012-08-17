pycon構想

pythonのサブセットでコンパイラとしての実装の実験
型を推論して、実行時ではなくコンパイル時に型を決定する。
型が決定できないときはエラーにする。

pycon1仕様
型は、整数と文字列のみ。
変数なし。
演算は+と*と=
式を評価して文字列として返す。
"で囲まれたものは文字列。
数字で構成されているのは数値。
"abc" + "def" -> "abcdef"
"abc" + 3 -> Error
3 + "abc" -> Error
3 + 4 -> "7"

"abc" * "def" -> Error
"abc" * 3 -> "abcabcabc"
3 * "abc" -> "abcabcabc"
3 * 4 -> "12"

でだしとしては、spark/example/paper/
をベースにする。

