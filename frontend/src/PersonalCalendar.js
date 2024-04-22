import React, { useEffect, useState } from 'react'
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'

import '@fullcalendar/daygrid/main.css'
import '@fullcalendar/list/main.css'
let url = 'http://127.0.0.1:8000'

const initEvents = [
    { title: 'All Day Event', start: getDate('YEAR-MONTH-01') },
    
]

function getDate(dayString) {
    const today = new Date()
    const year = today.getFullYear().toString()
    let month = (today.getMonth() + 1).toString()

    if (month.length === 1) {
        month = '0' + month
    }

    return dayString.replace('YEAR', year).replace('MONTH', month)
}

const PersonalCalendar = () => {
const [events, setEvents] = useState(initEvents)
// initEvents 為上面原本的 events
    useEffect(() => {getData()}, [])
    function getData() {
        fetch(url, {
        method: 'GET',
        redirect: 'follow',
     })
        .then((response) => response.json())
        .then((result) => {
            console.log(result)
            setEvents(result)
        })
        .catch((error) => console.log('error', error))
        }
    return (
        <div className='calendarContainer'>
            <FullCalendar
                events={events}
                plugins={[dayGridPlugin]}
                height='500px'
            />
        </div>
    )
}

export default PersonalCalendar