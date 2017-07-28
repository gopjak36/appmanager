function initDateFields() {
  $('.datep').datetimepicker({
    'format': 'YYYY-MM-DD'
  }).on('dp.hide', function(event){
    $(this).blur();
  });
}

function initTimeFields() {
  $('.timep').datetimepicker({
    'format': "HH:mm"
  }).on('dp.hide', function(event){
    $(this).blur();
  });
}

$(document).ready(function(){
  initDateFields();
  initTimeFields();
});
