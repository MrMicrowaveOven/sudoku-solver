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

function clearBoard() {
  $('.sudoku-space').val('')
}

function fillWithSample() {
  $('#space01').val(9)
  $('#space02').val(5)
  $('#space03').val(1)
  $('#space07').val(8)

  $('#space10').val(1)
  $('#space12').val(7)
  $('#space13').val(9)
  $('#space14').val(8)
  $('#space16').val(4)
  $('#space17').val(5)
  $('#space18').val(2)

  $('#space21').val(8)
  $('#space26').val(9)
  $('#space27').val(6)

  $('#space33').val(8)
  $('#space34').val(4)
  $('#space35').val(2)
  $('#space37').val(9)

  $('#space44').val(9)
  $('#space45').val(5)
  $('#space46').val(6)
  $('#space48').val(4)

  $('#space50').val(5)
  $('#space55').val(7)

  $('#space61').val(6)
  $('#space66').val(5)

  $('#space72').val(1)
  $('#space76').val(2)
  $('#space78').val(9)

  $('#space80').val(7)
}




function getMove() {
  $(".sudoku-space").prop('disabled', false);
  var spaces = [];
  var row = [];
  $('.sudoku-space').each(function(id, space) {
    if (id % 9 == 0 && id > 0) {
      spaces.push(row)
      row = []
    }
    if (space.value == '') {
      row.push(null)
    } else {
      row.push(parseInt(space.value))
    }

  })
  spaces.push(row)
  $.ajax({
      url: "http://localhost:5000/one_move",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify({"board": spaces})
    }).done(function(data) {
      placeMove(data)
  });
}

function placeMove(data) {
  if (data.invalid) {
    displayError(data.invalid)
  } else {
    move = data.move.space
    board = data.board
    newValue = board[move[0]][move[1]]
    moveString = move.join('')
    $('#space' + moveString).val(newValue)
    $('.sudoku-space').removeClass('font-red font-blue')
    $('#space' + moveString).addClass('font-blue')
  }
}

function displayError(invalidCoords) {
  $('.sudoku-space').removeClass('font-red font-blue')
  $('.error-message').removeClass('invisible')
  invalidCoords.forEach(function(invalidCoord) {
    invalidCoordString = invalidCoord.join('')
    $('#space' + invalidCoordString).addClass('font-red')
  })
}
