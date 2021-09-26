window.onload = function () {
    const socket = io.connect('/user');
    socket.on('test', (data) => {
        console.log(data);
    })
    
    socket.on('video', (data) => {
        $('#image').attr('src',`data:image/jpeg;base64,${data}`);
        
    })
    var sw;
    $('#onoff').on('click', (e) => {
        sw = $('#onoff').text() == 'on';
        if(sw) {
            $('#onoff').html('off');
        } else {
            $('#onoff').html('on');
            setTimeout(() => {
                $('#image').attr('src', '/images/videostop.jpg');
            }, 40)
        }
        socket.emit('vOnOff', sw);

    })
    
    
  socket.on('position1', (data) => {
    var x = []
    var y = []
    console.log(data[0]._id)
    $('#timeshow').html(`${cvDate(data[0]._id)} ~ ${cvDate(data[data.length-1]._id)}`)
      data.forEach((el) => {
       x = x.concat(el.x)
       y = y.concat(el.y)
      })
      var trace2 = {
        x: x, y: y,
        name: 'density',
        ncontours: 200,
        colorscale: 'Hot',
        reversescale: true,
        showscale: false,
        type: 'histogram2dcontour'
      };
      var data1 = [trace2];
      var layout = {
        width: 960,
        height: 540,
        xaxis: { range: [0, 960] },
        yaxis: { range: [540, 0] }
      };
      Plotly.newPlot('myDiv', data1, layout);
  });

  

    var x = [], y = [], z=[];
    Plotly.newPlot('myDiv', [{
      x: x,
      y: y,
      mode: 'markers',
      marker: {size: 10}
    }], {
      width: 960,
      height: 540,
      xaxis: { range: [0, 960] },
      yaxis: { range: [540, 0] }
    })
  socket.on('position', (data) => {
    function update() {
        $('#timeshow').html(`${cvDate(z)}`)
        Plotly.animate('myDiv', {
          data: [{ x: data.x, y: data.y }]
        }, {
          transition: {
            duration: 2
          },
          frame: {
            duration: 2,
            redraw: true
          }
        });
    }
    requestAnimationFrame(update);
  })
  function cvDate(date) {
    let convertDate = new Date(date);
    return "20/" + (convertDate.getMonth() + 1) + "/" + convertDate.getDate() + ", " + convertDate.getHours() + ":" + convertDate.getMinutes() + ":" + convertDate.getSeconds();
}
}
