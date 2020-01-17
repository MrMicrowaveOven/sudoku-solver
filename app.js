// Build Sudoku Grid
for (var i = 0; i < 9; i++) {
  var div = '<div class="row' + i + '"></div>'
  $('.sudoku-grid').append(div)
  for (var j = 0; j < 9; j++) {
    var text_field = '<input type="text" id="space' + i + j + '" name="" value="" class="sudoku-space" oninput="this.value = this.value.replace(/[^0-9.]/g, ``).replace(/(\..*)\./g, `$1`);">'
    $('.row' + i).append(text_field)
  }
  $('.row' + i).append('<br>')
}

$('.sudoku-space').each(function(i, el) {
  var classList = $(this).attr('id').split('space')
  var spaceId = classList[classList.length - 1]
  var firstDigit = spaceId[0]
  var secondDigit = spaceId[1]
  var isGray = firstDigit < 3 && secondDigit < 3
  isGray += firstDigit < 3 && secondDigit > 5
  isGray += (firstDigit >= 3 && firstDigit <= 5) && (secondDigit >= 3 && secondDigit <= 5)
  isGray += firstDigit > 5 && secondDigit < 3
  isGray += firstDigit > 5 && secondDigit > 5
  if (isGray) {
    $(this).addClass('gray')
  }

})



$.ajax({
      url: "http://localhost:5000",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify({"message": 'message'})
  }).done(function(data) {
      console.log(data);
  });
