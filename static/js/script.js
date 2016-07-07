// Page javascript
$(function(){
    var xeditable_options = {};
    datatableview.initialize($('.editable'), {
        fnRowCallback: datatableview.make_xeditable(xeditable_options)
    });
    // Fill modal with content from link href
    $("#myModal").on("show.bs.modal", function(e) {
        var link = $(e.relatedTarget);
        $(this).find(".modal-content").load(link.attr("href"));
    });

    $("select").chosen().change(function(event){

     if(event.target == this && this.id == "id_wood_kind"){
         address = "/" + $(this).val() + "/price/";
         $.get( address, function( data ) {
             $( "input[id=id_detail_price]" ).val( Number(data.replace(',','.')) );
        });
     }

     if(event.target == this && this.id == "id_contractor"){
         address = "/" + $(this).val() + "/shipment/";
         $(".order-filter").attr("href", address);
     }

    });

    $('#id_date').datepicker({
        format: "yyyy-mm-dd",
        startView: "decade",
        minViewMode: "days",
        language: 'pl'
    });

    $('#id_month').datepicker({
        format: "yyyy/mm",
        startView: "months",
        minViewMode: "months",
        language: 'pl'
    }).change(function(event) {
        address = "/" + $(this).val() + "/";
        $(".order-filter").attr("href", address);
    });


    $(function () {
      $('[data-toggle="tooltip"]').tooltip()
    });

});

