const cities = [
    "Paris?", "Tokyo?", "London?", "New York?", "Sydney?",
    "Hong Kong?", "Shanghai?", "Rome?", "Los Angeles?", "Dubai?",
    "Moscow?", "Berlin?", "Cairo?", "Rio de Janeiro?", "Bangkok?"
  ];
  const destinationElement = document.getElementById("destination");

function typeAndDeleteEffect() {
    let cityIndex = 0;
    let isTyping = true;
    let text = "";

    function type() {
        text = cities[cityIndex].substring(0, text.length + 1);
        destinationElement.innerHTML = text;

        if (text === cities[cityIndex]) {
            isTyping = false;
            setTimeout(deleteText, 1000);
        } else {
            setTimeout(type, 150);
        }
    }

    function deleteText() {
        text = cities[cityIndex].substring(0, text.length - 1);
        destinationElement.innerHTML = text;

        if (text === "") {
            isTyping = true;
            cityIndex = (cityIndex + 1) % cities.length;
            setTimeout(type, 500);
        } else {
            setTimeout(deleteText, 50);
        }
    }
    type();
}

typeAndDeleteEffect();
