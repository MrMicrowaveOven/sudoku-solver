// Build Sudoku Grid
var text_field = '<input type="text" name="" value="" class="sudoku-space">'
for (var i = 0; i < 9; i++) {
  var div = '<div class="row' + i + '"></div>'
  $('.sudoku-grid').append(div)
  for (var j = 0; j < 9; j++) {
    $('.row' + i).append(text_field)
  }
  $('.row' + i).append('<br>')
}


$.ajax({
      url: "http://localhost:5000",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify({"message": 'message'})
  }).done(function(data) {
      console.log(data);
  });
