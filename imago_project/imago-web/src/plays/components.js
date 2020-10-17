import React, {useEffect, useState} from 'react';
import {Link} from 'react-router-dom';
import {loadListOrDetail, loadImage, loadCacheImage} from '../lookup';
import { MemberList } from '../members/components';


function PlayListItem(props) {
    const {play} = props
    const cls = props.className ? props.className : 'card'
    const cover = loadImage(play.get_cover)
        
    return (
        <Link to={`plays/${play.slug}`}>
            <div className={cls}>
                <img    src={cover} 
                        className="card-img-top card-cover" 
                        alt="Cover" />
                <div className="card-body">
                    <h5 className="card-title">{play.title}</h5>
                    <ShowDescriptionBtn play={play}/>
                </div>
            </div>
        </Link>
    )
}

function ShowDescriptionBtn(props) {
    const {play} = props.play

    const handleClick = (event) => {
        event.preventDefault()
        console.log(play.description)
    }
    return (
    <button className="btn btn-primary" 
            onClick={handleClick}>
            Show Description
    </button>
    )
    
}
  
export function PlayList() {
    const [plays, setPlays] = useState([])

    useEffect(() => {
    const myCallback = (response, status) => {
        if (status === 200) {
            setPlays(response)
        } else {
            alert("There was an error")
        }
    }
    loadListOrDetail(myCallback, "plays")
    }, [])

    return plays.map((item, index)=>{
    return <PlayListItem play={item} key={`${index}-${item.slug}`} className='card text-white bg-dark my-2 mx-2'/>
    })
}

function GalleryListItem(props) {
    // const img_url = props.image.cache_url + "/" + props.image.image_filename
    const file = props.image.thumbnail
    const image_url = loadCacheImage(file)
    return (
        <div className="galleryListItem">
            <img src={image_url} alt="Play gallery img"/>
        </div>
    )
}


function GalleryList(props) {
    const galleryItems = props.galleryList.photos
    return galleryItems.map((item, index)=>{
        if (item) {
            return (
                <GalleryListItem image={item} key={`${index}`} />
                )
        } else {
            return (
                <div className="spinner-border text-danger" role="status">
                    <span className="sr-only">Loading...</span>
                </div>
            )
        }
        
    })
}

export function PlayDetail({ match }) {
    const [play, setPlay] = useState()
    useEffect(() => {
        const myCallback = (response, status) => {
            if (status === 200) {
                setPlay(response)
                console.log(response)
            } else {
                alert("There was an error")
            }
        }
        loadListOrDetail(myCallback, "plays", slug)
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])

    const slug = match.params.slug;



    if (play) {
        const cover_url = loadImage(play.get_cover)
        return  (
            <div className="container-fluid">
                <h1>{play.title}</h1>
                <div className="row">
                    <div className="col-sm displayCover">
                        <img src={cover_url} alt="Play cover"/>
                    </div>
                    <div className="col-9">
                        <p>{play.description}</p>
                    </div>
                </div>
                <h2>Members</h2>
                <MemberList members={play.members}/>
                {play.gallery ? (
                            <>
                            <h2>Gallery</h2>
                            <div className="gallery">
                                <GalleryList galleryList={play.gallery} /> 
                            </div>
                            </>
                        ):(
                            <></>
                        )}
            </div>
    )
    }   else {
        return (
            <div className="spinner-border text-danger" role="status">
                <span className="sr-only">Loading...</span>
            </div>
        )
    }
}