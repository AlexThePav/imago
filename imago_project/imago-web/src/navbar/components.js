import React from 'react';
import {Link} from 'react-router-dom';

function NavItem (props) {
    const href = props.href
    const name = props.name

    if (props.isLogo === true) {
        return (
            <a className="navbar-brand" href={href}>
                <img src="/pixel-butterfly.jpg"
                    width="50" 
                    height="50" 
                    alt="" 
                    loading="lazy"/>
            </a>
        )
    }

    return (
        <li className={props.className} onClick={props.onClick}>
            <Link to={href} className="nav-link" >{name}</Link>
        </li>
    )
}


export class NavBar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            navs: [0, 1, 2, 3, 4],
            activeNav: null,
            navClassName: "nav-item",
        }
    }

    handleClick(i) {
        const navs = this.state.navs.slice();
        this.setState({
            activeNav: navs[i]
        });
    }

    renderNav(i, name, href, isLogo) {
        let navClassName = this.state.navClassName
        if (href === window.location.pathname) {
            navClassName = navClassName + " active"
        }
        return (
            <NavItem 
                name={name} 
                href={href}
                className={navClassName}
                isActive={this.state.isNavActive}
                isLogo={isLogo}
                onClick={() => this.handleClick(i)}
            />
        );
    }

    render() {
        return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            {this.renderNav(0, "Home", "/", true)}
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggler" aria-controls="navbarToggler" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>

            <div className="collapse navbar-collapse" id="navbarToggler">
                <ul className="navbar-nav mr-auto mt-2 mt-lg-0">
                    {this.renderNav(1, "Plays", "/plays", false)}
                    {this.renderNav(2, "Members", "/members", false)}
                    {this.renderNav(3, "About", "/about", false)}
                    {this.renderNav(4, "Contact", "/contact", false)}
                </ul>
                <div className="d-inline-flex">
                <div className="input-group">
                    <input type="text" className="form-control" placeholder="Search" aria-label="Recipient's username" aria-describedby="button-addon2"/>
                    <div className="input-group-append">
                        <button className="btn btn-outline-secondary" type="button" id="button-addon2">Search</button>
                    </div>
                </div>
                </div>
            </div>
        </nav>
        )
    }
    
}