import React, {useEffect, useState} from 'react';
import {loadPlays} from '../lookup';

function PlayListItem(props) {
  const {play} = props
  const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
  return <div className={className}>
    <p>{play.title}</p>
    <ShowDescriptionBtn play={play}/>
  </div>
}

function ShowDescriptionBtn(props) {
  const {play} = props
  const handleClick = (event) => {
      event.preventDefault()
      console.log(play.description)
  }
  return <button onClick={handleClick}>Show Description</button>
}
  
export function PlayList(props) {
  const [plays, setPlays] = useState([])

  useEffect(() => {
    const myCallback = (response, status) => {
      console.log(response, status)
      if (status === 200) {
        setPlays(response)
      } else {
        alert("There was an error")
      }
    }
    loadPlays(myCallback)
  }, [])
  return plays.map((item, index)=>{
    return <PlayListItem play={item} key={`${index}-{item.slug}`} className='my-5 py-5 px-3 border' />
  })
}
