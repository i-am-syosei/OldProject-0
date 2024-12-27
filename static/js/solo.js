'use strict';
  
// import shuffle from './shuffle';
document.addEventListener('DOMContentLoaded',()=>{
  // const card = new Card("heart",1);

  //Cardクラス作成
  class Card{
    constructor(suit,num){ 
      //カードのスート(s:スペード、d:ダイヤ)
      this.suit=suit;
      //カードの数字(1,2,...13)
      this.num=num;
      //カードの画像
      this.front=`${suit}${num}.png`;
    }
  }
  //引いた枚数
  let count = 0
  //プレイヤー
  let player1 = null;
  let player2 = null;
  //プレイヤーが引いた枚数
  let player1point = 0;
  let player2point = 0;
  //カード配列作成
  window.cards=[];
  //カードスーツ配列
  const suits=['s','d'];
  //2重forで52枚のカードを作成
  for(let i=0;i<suits.length;i++){
    for(let j=1;j<=16;j++){
      //カードインスタンス生成(s1,s2....c13)
      let card=new Card(suits[i],j);
      //配列の末尾に追加
      window.cards.push(card);
    }
  }
  let firstCard=null;//1枚目のカードを保持(引いてない場合はnull)
  let secondCard=null;//2枚目のカードを保持(引いてない場合はnull)
  if(player1 == null && player2 == null){
    player1 = "player";
  }
  
  //クリックした際の関数を定義
  const flip=(eve)=>{
    
    //クリックされた要素を特定
    let div=eve.target;

    if(!div.classList.contains('back') || secondCard !== null){
      return;
    }
    //表面にする
    div.classList.remove('back');
    //もしそれが1枚目だったらfirstCardに代入
    if(firstCard === null){
      firstCard=div;
    }else{
      //2枚目だったらsecondCardに代入
      secondCard=div;
      //２枚のカードの数字が同じだったら
      if(firstCard.num === secondCard.num){
        //正解だった場合fadeoutクラスを付与する
        firstCard.classList.add('fadeout');
        secondCard.classList.add('fadeout');
        //firstCard,secondカードを共にnullに戻す
        [firstCard,secondCard]=[null,null];
        //引かれた枚数を数える
        count++;
        //player1が引いた場合得点加算
        if(player1 == "player"){
          player1point++;
        }else{
        //player2が引いた場合得点加算  
          player2point++;
        }
      
        // document.getElementById('input1').innerHTML = player1point;
        // document.getElementById('input2').innerHTML = player2point;
        
        //すべてのトランプを引くと終了結果表示
        if(count == 16){
        document.getElementById("area_time").innerHTML = TimeLapsed();
        localStorage.setItem('elapsedTime', TimeLapsed());
           window.location.replace('./soloresult');
        }


      }else{
        //不正回だった場合は1.2秒後に裏面に戻す
        setTimeout(()=>{
          firstCard.classList.add('back');
          secondCard.classList.add('back');
          [firstCard,secondCard]=[null,null];
          //player1がペアを引けなかった場合player2に交
        },1200);
        
        
        
        
      }
    }
    
  };
  //cardgridのDOM取得
  const cardgrid=document.getElementById('cardgrid');
  //gridを初期化する処理
  const initgrid=()=>{
    //cardgridに入っている要素をすべて削除
    cardgrid.textContent=null;
    for(let i=0;i<suits.length;i++){
      for(let j=0;j<16;j++){
        //１枚毎のトランプとなるdiv要素作成
        let div=document.createElement('div');
        //配列からcardを取り出す
        let card=window.cards[i*16+j];
        //背景画像に画像を設定
        div.style.backgroundImage=`url(../static/images/${card.front})`;
        //divにcardクラスとbackクラス追加
        div.classList.add('card','back');
        //要素をクリックした際の挙動を登録
        div.onclick=flip;
        //divにnumプロパティを定義して、そこに数字を保存
        div.num=card.num;
        //cardgrid要素に追加
        cardgrid.append(div);
      }
    }
  };

  window.onload = function () {
    count = 0;
    // shuffle関数を別ファイルから呼び出す
    const shuffledCards = shuffle(cards);
    initgrid(shuffledCards);
    [firstCard,secondCard]=[null,null];
  }
});



function TimeFormat(time_h,time_m,time_s){
  var str = "";
  var tmp;
  if(time_h < 100){
    tmp = "00" + String( time_h );
    str += tmp.substr(tmp.length - 2);
  }else{
    str += String( time_h );
  }
  str += ":";
  tmp = "00" + String( time_m );
  str += tmp.substr(tmp.length - 2);
  return str;
}

// 表示された時間を取得する
var time_view = parseInt((new Date)/1000);

// 経過時間を表示する
function TimeLapsed(){
  var now_unixtime = parseInt((new Date)/1000);
  var tmp = now_unixtime - time_view;
  var time_h = Math.floor(tmp/3600);
  var time_m = Math.floor(tmp/60);
  var time_s = tmp - time_m*60 - time_h*3600;

  return TimeFormat(time_m,time_s);
}

function TimeFormat(minutes, seconds) {
  // 時間のフォーマットを整形する処理が必要
  return `${minutes}:${seconds}`;
}

function saveAndNavigate() {
  // ローカルストレージに経過時間を保存
  localStorage.setItem('elapsedTime', TimeLapsed());
}

function TimeLapsedView() {
  document.getElementById("area_time").innerHTML = TimeLapsed();
  setTimeout(TimeLapsedView, 100);
}
TimeLapsedView();

// 経過時間をdiv領域に表示する動作を一定間隔で繰り返す
function TimeLapsedView(){
  document.getElementById("area_time").innerHTML = TimeLapsed();
  setTimeout("TimeLapsedView()",100);
}
TimeLapsedView();
