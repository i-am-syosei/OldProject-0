// Fisher-Yates シャッフル関数を定義
const shuffle = (cards) => {
  let i = cards.length;
  while (i) {
    let index = Math.floor(Math.random() * i--);
    [cards[index], cards[i]] = [cards[i], cards[index]]
  }
  return cards;
};
