// Build Sudoku Grid
    // for (var i = 0; i < array.length; i++) {
    //   array[i]
    // }


$.ajax({
      url: "http://localhost:5000",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify({"message": 'message'})
  }).done(function(data) {
      console.log(data);
  });
