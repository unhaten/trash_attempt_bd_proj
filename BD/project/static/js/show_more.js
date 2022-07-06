function readMore() {
    var dots = document.getElementById('dots');
    var more = document.getElementById('more');
    var btn_more = document.getElementById('btn_more');

    if (dots.style.display === 'none') {
        dots.style.display = 'inline';
        btn_more.innerHTML = 'Show Info';
        more.style.display = 'none';
    } else {
        dots.style.display = 'none';
        btn_more.innerHTML = 'Hide';
        more.style.display = 'inline';
    }
}

function revealMore() {
    var blank_text = document.getElementById('blank_option');
    var text_area = document.getElementById('text_area')

    if (this.value !== blank_text) {
        var library = this.value;
        text_area.value = library;


    }
}

function searchMore() {
    var text_area = document.getElementById('text_area');
    var adress_area = document.getElementById('adress');
    // adress_area = text_area;
    text_area.value = 'Info is below'
    adress_area.innerHTML = adress_area.innerHTML.replace('None', text_area.value);
    // text_area.value = adress_area.value;

}

// var element = document.getElementById("kamal");
// var selectedValue = element.options[element.selectedIndex].text;


document.getElementById('shop_select').addEventListener('change', revealMore);