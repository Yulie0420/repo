import React, { useEffect, useState } from 'react'

let url = 'http://127.0.0.1:8000'
let val = {
    id: 0,
    data: ['03/22', '13:00', 'www', 'qqq'],
}

const PersonalCalendar = () => {
    function postData(url, data) {
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
            redirect: 'follow',
        }

        fetch(`${url}/addNewEvents`, requestOptions)
            .then((response) => response.json())
            .then((result) => console.log(result))
            .catch((error) => console.log('error', error))
    }
    function getData() {
        fetch(url, {
            method: 'GET',
            redirect: 'follow',
        })
            .then((response) => response.json())
            .then((result) => console.log(result))
            .catch((error) => console.log('error', error))
    }
    useEffect(() => {}, [])
    return (
        <div>
            PersonalCalendar
            <button
                onClick={() => {
                    postData(url, val)
                }}
            >
                post
            </button>
            <button onClick={getData}>getData</button>
        </div>
    )
}

export default PersonalCalendar