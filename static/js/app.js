 //Get the button
 let mybutton = document.getElementById("btn-back-to-top");

 // When the user scrolls down 20px from the top of the document, show the button
 window.onscroll = function () {
   scrollFunction();
 };
 
 function scrollFunction() {
   if (
     document.body.scrollTop > 20 ||
     document.documentElement.scrollTop > 20
   ) {
     mybutton.style.display = "block";
   } else {
     mybutton.style.display = "none";
   }
 }
 // When the user clicks on the button, scroll to the top of the document
 mybutton.addEventListener("click", backToTop);
 
 function backToTop() {
   document.body.scrollTop = 0;
   document.documentElement.scrollTop = 0;
 }

 // Cari judul buku
const tombol = document.getElementById("tombol");
const search = document.getElementById("searchKamusTitle");
const none = document.getElementById("tidak-ada");


// Cari judul buku
localStorage.setItem('itemCount', '0');
search.addEventListener("keyup", function () {
  const itemCount = Number(localStorage.getItem('itemCount'));
  
  const List = document.getElementsByClassName("text-kamus");
  console.log(itemCount);
  let numOfList = 0;

  for (const kamusItem of List) {
    if (!kamusItem.innerHTML.toLowerCase().includes(search.value.toLowerCase())) {
      kamusItem.parentNode.parentNode.style.display = "none";
      // numOfList += 1;
    } else {
      kamusItem.parentNode.parentNode.style.display = "flex";
      numOfList += 1;
    }
  }
  
  console.log(numOfList);
  localStorage.setItem('itemCount', numOfList);
  
  const noKamus = document.getElementById('no-kamus');
  if (itemCount < 1) {
    noKamus.style.display = "block";
  } else {
    noKamus.style.display = "none";
  }
  
});