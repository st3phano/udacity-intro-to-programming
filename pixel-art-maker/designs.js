/*
 * @desc create a grid of squares of height x width
 * @param object $event - the event object
 */
function makeGrid(event) {
    grid.textContent = ''; //delete the last canvas
    
    const height = sizePicker[0].value;
    const width = sizePicker[1].value;
    
    for(let row = 1; row <= height; ++row)
    {
        const newRow = document.createElement('tr');
        grid.appendChild(newRow);
        
        for(let column = 1; column <= width; ++column)
        {
            const newCell = document.createElement('td');
            newRow.appendChild(newCell);
        }
    }  
    
    event.preventDefault(); //prevent page from updating
}

/*
 * @desc color a cell inside the grid according to the value chosen using the color selector
 * @param object $event - the event object
 */
function colorCell(event) {
    const color = colorPicker.value;
    if(event.target.nodeName === 'TD') //clicks only work inside cells
    {
        event.target.style.background = color;
    }
    
}

const sizePicker = document.querySelector('#sizePicker');
const colorPicker = document.querySelector("#colorPicker");
const grid = document.querySelector('#pixelCanvas');

const submitButton = sizePicker[2];

submitButton.addEventListener('click', makeGrid);
grid.addEventListener('click', colorCell);