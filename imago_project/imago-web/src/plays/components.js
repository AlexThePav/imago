import React, {useEffect, useState} from 'react';
import {loadPlays} from '../lookup';

function PlayListItem(props) {
    const {play} = props
    const className = props.className ? props.className : 'card'
    const backendUrl = "http://localhost:8000/media/photologue/photos/"
    let cover;
    if (play.cover !== null) {
        cover = backendUrl + play.cover.image_filename
    } else {
        cover = "..."
    }
    return (
    <div className={className}>
        <img src={cover} className="card-img-top" alt="Cover" id="card-cover" />
        <div className="card-body">
            <h5 className="card-title">{play.title}</h5>
            <p className="card-text">Short play description</p>
            <ShowDescriptionBtn play={play}/>
        </div>
        
    </div>
    )
}

function ShowDescriptionBtn(props) {
    const {play} = props
    const handleClick = (event) => {
        event.preventDefault()
        console.log(play.description)
    }
    return <button className="btn btn-primary" onClick={handleClick}>Show Description</button>
}
  
export function PlayList(props) {
    const [plays, setPlays] = useState([])

    useEffect(() => {
    const myCallback = (response, status) => {
        if (status === 200) {
        setPlays(response)
        } else {
        alert("There was an error")
        }
    }
    loadPlays(myCallback)
    }, [])

    return plays.map((item, index)=>{
    return <PlayListItem play={item} key={`${index}-{item.slug}`} className='card text-white bg-dark my-2 mx-2' />
    })
}
