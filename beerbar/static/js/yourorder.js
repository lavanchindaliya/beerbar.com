var currentPage = "your order's";
    var navTag = document.querySelector('.order');
    if(currentPage == navTag.innerText.toLowerCase()){
        navTag.style.backgroundColor = 'gold'
        navTag.style.color = 'black'
    }