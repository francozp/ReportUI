//exporte les données sélectionnées
var $table = $('#table');
    $(function () {
        $('#toolbar').find('select').change(function () {
            $table.bootstrapTable('refreshOptions', {
                exportDataType: $(this).val()
            });
        });
    })

		var trBoldBlue = $("table");

	$(trBoldBlue).on("click", "tr", function (){
			$(this).toggleClass("bold-blue");
    });
    
$(function () {
    $('#table').bootstrapTable({
        data: data
    });
    $('#table').on('check.bs.table', function (e, row, $el) {
        alert('check index: ' + $el.closest('tr').data('index'));
    });
    $('#table').on('uncheck.bs.table', function (e, row, $el) {
        alert('uncheck index: ' + $el.closest('tr').data('index'));
    });
});