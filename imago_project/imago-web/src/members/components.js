import React, {useEffect, useState} from 'react';
import {Link} from 'react-router-dom';

import {loadListOrDetail, loadImage} from '../lookup';

function MemberListItem(props) {
    const {member} = props
    const className = props.className ? props.className : 'card'
    const profile_pic = loadImage(member.get_profile_pic)
    return (
    <Link to={`members/${member.slug}`}>
        <div className={className}>
            <img src={profile_pic} className="card-img-top card-cover" alt="Profile pic" />
            <div className="card-body">
                <h5 className="card-title">{member.full_name}</h5>
            </div>
        </div>
    </Link>
    )
}

export function MemberList() {
    const [members, setMembers] = useState([])

    useEffect(() => {
    const memberCallBack = (response, status) => {
        if (status === 200) {
            setMembers(response)
        } else {
            alert("There was an error")
        }
    }
    loadListOrDetail(memberCallBack, "members")
    }, [])

    return members.map((item, index)=>{
    return <MemberListItem member={item} key={`${index}-${item.slug}`} className='card text-white bg-dark my-2 mx-2' />
    })
}

export function MemberDetail({ match }) {
    const slug = match.params.slug
    const [member, setMember] = useState()

    useEffect(() => {
        const myCallback = (response, status) => {
            if (status === 200) {
                setMember(response)
            } else {
                alert("There was an error")
            }
        }
        loadListOrDetail(myCallback, "members", slug)
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])

    if (member) {
        return  (
            <div>
                <h1>{member.full_name}</h1>
                <p>{member.email}</p>
            </div>
    )
    }   else {
        return <p>Loading...</p>
    }
}