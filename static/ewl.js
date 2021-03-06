$(function(w){

const btnEatClick = (e) => {
    $("#modalEat").modal();

    const req = {
        url: "/food",
        method: "get"
    };

    const promise = $.ajax(req);

    const success = function(data) {
        const foodList = data["foods"];
        let i;
        $("#selectFood").empty();

        for(i=0;i<foodList.length;i++){
            let optionFood = $("<option>" + foodList[i].name + "</option>");
            optionFood.val(foodList[i].id);
            $("#selectFood").append(optionFood);
        }
    };

    const failure = function(res) {
        alert("I'm sorry. I couldn't get a list of food from home base.");
    };
    
    promise.then(success, failure);
};

const btnAddFoodClick = (e) => {
    const newFoodJson = {
        "new_food": $("#txtNewFood").val()
    };

    const req = {
        method: "post",
        url: "/food",
        headers: {
            "Content-type": "application/json"
        },
        data: JSON.stringify(newFoodJson)
    };

    const success = function(data){
        alert(data.msg);
        const foodList = data["foods"];
        let i;
        $("#selectFood").empty();

        for(i=0;i<foodList.length;i++){
            let optionFood = $("<option>" + foodList[i].name + "</option>");
            optionFood.val(foodList[i].id);
            $("#selectFood").append(optionFood);
        }

        $("#txtNewFood").val("")
    };
    const failure = function(data){};

    const promise = $.ajax(req);
    promise.then(success, failure);
};

const btnWeighClick = (e) => {
    $("#modalWeigh").modal();
};

const btnLoveClick = (e) => {
    $("#modalLove").modal();
};

const btnWeightHistoryClick = (e) => {
    $("#modalWeightHistory").modal();
};

const btnAddServingClick = (e) => {
    const foodID = $("#selectFood").val();
    const numPortions = $("#numPortions").val();
    let jsonData = {
        "food_id": foodID,
        "portions": numPortions
    };

    jsonData = JSON.stringify(jsonData);

    const req = {
        url: "/serving",
        method: "post",
        headers: {
            "Content-type": "application/json"
        },
        data: jsonData
    };

    const success = function(e){
        console.log("serving addition success...");
        console.log(e);
    };

    const failure = function(e){
        console.log("serving addition failed...");
        console.log(e);
    };

    const promise = $.ajax(req);
    promise.then(success, failure);
}

$("#btnEat").on("click", btnEatClick);
$("#btnAddNewFood").on("click", btnAddFoodClick);
$("#btnWeigh").on("click", btnWeighClick);
$("#btnLove").on("click", btnLoveClick);
$("#btnWeightHistory").on("click", btnWeightHistoryClick);

$("#btnAddServing").on("click", btnAddServingClick);


}(window));