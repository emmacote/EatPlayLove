$(function(w){

const btnEatClick = function(e){
    $("#modalEat").modal();
};

const btnWeighClick = function(e){
    $("#modalWeigh").modal();
};

const btnLoveClick = function(e){
    $("#modalLove").modal();
};

const btnWeightHistoryClick = function(e){
    $("#modalWeightHistory").modal();
};

$("#btnEat").on("click", btnEatClick);
$("#btnWeigh").on("click", btnWeighClick);
$("#btnLove").on("click", btnLoveClick);
$("#btnWeightHistory").on("click", btnWeightHistoryClick);


}(window));