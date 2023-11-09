def add_time(start, duration, day_of_week = None):

  # Convert start into a list of [hours, minutes] in 24h format
  start_clock, start_period = start.split(' ')
  start_hours = start_clock.split(':')[0]
  start_minutes = start_clock.split(':')[1]

  start_hours = int(start_hours)
  start_minutes = int(start_minutes)
  
  if start_period == 'PM':
    start_hours += 12

  # Convert duration to [hours, minutes]
  duration_hours = duration.split(':')[0]
  duration_minutes = duration.split(':')[1]

  duration_hours = int(duration_hours)
  duration_minutes = int(duration_minutes)
  
  # Add duration to start
  days = 0
  end_hours = start_hours + duration_hours 
  end_minutes = start_minutes + duration_minutes
  
  if end_minutes > 60:
    end_hours += int(end_minutes / 60)
    end_minutes = end_minutes % 60
  
  if end_hours >= 24:
    days += int(end_hours / 24)
    end_hours = end_hours % 24

  days_later = ''
  if days == 1:
    days_later += ' (next day)'
  if days > 1:
    days_later += f' ({days} days later)'

  # Convert end time back to 12h format
  # end_hours goes from 0 to 23
  end_period = 'AM'
  
  if end_hours == 0:
    end_hours += 12
  elif end_hours >= 12:
    end_period = 'PM'
    
  if end_hours >= 13:
    end_hours -= 12

  # Assemble new time string and add preceding zero to minutes if necessary
  new_minutes = '0' + str(end_minutes) if end_minutes < 10 else str(end_minutes)
  
  new_time = f'{str(end_hours)}:{new_minutes} {end_period}'
  if day_of_week:
    new_time += ', ' + weekday(day_of_week, days)
  new_time += days_later
  
  return new_time


# Function that takes a day of the week and the number of days to be added to it
# Returns the end day of the week, capitalized
def weekday(start, days):

  start_day = start.lower().capitalize()
  weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
              'Friday', 'Saturday', 'Sunday']

  start_index = weekdays.index(start_day)
  end_index = start_index + (days % 7)
  if end_index > 6:
    end_index -= 7
  
  end = weekdays[end_index]
  
  return end