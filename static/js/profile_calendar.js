<script>
  $(document).ready(function() {
    // Get the list of booked workshifts
    var bookedWorkshifts = [
      {% for booked_workshift in profile.booked_workshifts.all %}
        {
          title: '{{ booked_workshift.name }}',
          start: '{{ booked_workshift.start_time|date:"Y-m-d" }}',
          end: '{{ booked_workshift.end_time|date:"Y-m-d" }}'
        }{% if not forloop.last %},{% endif %}
      {% endfor %}
    ];

    // Initialize FullCalendar
    $('#calendar').fullCalendar({
      header: {
        left: 'prev,next today',
        center: 'title',
        right: 'month,agendaWeek,agendaDay'
      },
      events: bookedWorkshifts
    });
  });
</script>
