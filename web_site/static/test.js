//test	

let myMap

ymaps.ready(init)

function init(){
	console.log('load')
	let api = '0bd996a4-badf-46ed-b4fc-748760a4da64'
	myMap = new ymaps.Map('map', {
			center: [55.032697, 44.493349],
			zoom: 13
		}, {
				searchControlProvider: 'yandex#search'
			})
}
