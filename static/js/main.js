'use strict';

document.addEventListener('DOMContentLoaded', () => {

  class Card {
    constructor(suit, num) {
      this.suit = suit;
      this.num = num;
      this.front = `${suit}${num}.png`;
    }
  }

  let count = 0
  let player1 = null;
  let player2 = null;
  let player1point = 0;
  let player2point = 0;

  window.cards = [];

  const suits = ['s', 'd'];

  for (let i = 0; i < suits.length; i++) {
    for (let j = 1; j <= 16; j++) {
      let card = new Card(suits[i], j);
      window.cards.push(card);
    }
  }

  let firstCard = null;
  let secondCard = null;

  if (player1 == null && player2 == null) {
    player1 = "player";
  }

  const flip = (eve) => {
    let div = eve.target;

    if (!div.classList.contains('back') || secondCard !== null) {
      return;
    }

    div.classList.remove('back');
    if (firstCard === null) {
      firstCard = div;
    } else {
      secondCard = div;
      if (firstCard.num === secondCard.num) {
        firstCard.classList.add('fadeout');
        secondCard.classList.add('fadeout');
        [firstCard, secondCard] = [null, null];
        count++;

        if (player1 == "player") {
          player1point++;
        } else {
          player2point++;
        }

        document.getElementById('input1').innerHTML = player1point;
        document.getElementById('input2').innerHTML = player2point;

        if (count == 16) {
          
          sessionStorage.setItem("result1", player1point);
          sessionStorage.setItem("result2", player2point);
          window.location.replace('./result');

        }


      } else {

        setTimeout(() => {
          firstCard.classList.add('back');
          secondCard.classList.add('back');
          [firstCard, secondCard] = [null, null];

          if (player1 == "player") {
            player1 = null;
            player2 = "player";
          } else {
            player1 = "player";
            player2 = null;
          }
          if (player1 == "player") {
            document.getElementById('turn1').innerHTML = "引いてください";
            document.getElementById('turn2').innerHTML = "";
          } else {
            document.getElementById('turn2').innerHTML = "引いてください";
            document.getElementById('turn1').innerHTML = "";
          }
        }, 1200);

      }
    }

  };

  const cardgrid = document.getElementById('cardgrid');
  const initgrid = () => {
    cardgrid.textContent = null;
    for (let i = 0; i < suits.length; i++) {
      for (let j = 0; j < 16; j++) {
        let div = document.createElement('div');
        let card = window.cards[i * 16 + j];

        div.style.backgroundImage = `url(../static/images/${card.front})`;
        div.classList.add('card', 'back');
        div.onclick = flip;
        div.num = card.num;

        cardgrid.append(div);
      }
    }
  };

  document.getElementById('input1').innerHTML = player1point;
  document.getElementById('input2').innerHTML = player2point;

  window.onload = function () {
    count = 0;
    const shuffledCards = shuffle(cards);
    initgrid(shuffledCards);
    [firstCard, secondCard] = [null, null];
  }
});
