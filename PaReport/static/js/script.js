jQuery( document ).ready(function() {
    var ListItems = $('#tableselector').data('dynatable').settings.dataset.originalRecords;
    jQuery(ListItems).table_download({
        format: "csv",
        separator: "-",
        filename: "download",
        linkname: "Export CSV",
        quotes: "\""
    });    
    
});


