function drawStepperAreaChart(title,vAxisTitle,plotData,ID){
    var data_from_django = plotData;
    var data=google.visualization.arrayToDataTable(data_from_django);

    var options = {
        title: title,

        vAxis: {title: vAxisTitle},
        legend: { position: 'bottom' },
        isStacked: true

    };

    var chart = new google.visualization.SteppedAreaChart(document.getElementById(ID));
    chart.draw(data, options);

}


function drawLineChart(title,vAxisTitle,plotData,ID){
    var data_from_django = plotData;
    var data=google.visualization.arrayToDataTable(data_from_django);

    var options = {
        title: title,
        vAxis: {title: vAxisTitle},
        legend: { position: 'bottom' },
    };

    var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));
        chart.draw(data, options);
}