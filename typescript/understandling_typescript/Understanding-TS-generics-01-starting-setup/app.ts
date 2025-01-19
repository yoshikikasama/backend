// Code goes here!
// generic型とは他の特定の型と結合された型です。
// 例1）Array<string> (他の型はstring)
// 例2）Array<number> (他の型はnumber)
const names: Array<string> = [];

const promise = new Promise<string>((resolve, reject) => {
  setTimeout(() => {
    resolve("done");
  }, 200);
});
