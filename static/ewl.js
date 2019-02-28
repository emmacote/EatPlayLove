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
            let optionFood = $("<option>" + foodList[i] + "</option>");
            optionFood.val(foodList[i]);
            $("#selectFood").append(optionFood);
        }
    };

    const failure = function(res) {
        alert("eat failure");
    };
    
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

$("#btnEat").on("click", btnEatClick);
$("#btnWeigh").on("click", btnWeighClick);
$("#btnLove").on("click", btnLoveClick);
$("#btnWeightHistory").on("click", btnWeightHistoryClick);


}(window));