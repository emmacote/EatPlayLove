$(function(w){

const btnEatClick = (e) => {
    $("#modalEat").modal();
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