// get elements for popup

const popupbtn = document.querySelector('#update_button');

const popup = document.querySelector('.popup-wrapper');

const popupclose = document.querySelector('.popup-close');

// popup

popupbtn.addEventListener('click', () => {

    popup.style.display = "block";


});

popupclose.addEventListener('click', () => {

    popup.style.display = 'none';

});

popup.addEventListener('click', (e) => {

    if (e.target.className === 'popup-wrapper') {

        popup.style.display = 'none';

    }

});