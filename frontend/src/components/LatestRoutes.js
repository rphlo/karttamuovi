import React from 'react'
import { Link } from 'react-router-dom'
import moment from 'moment';
import LazyLoad from "vanilla-lazyload";

const LatestRoute = () => {
    const [routes, setRoutes] = React.useState(false)


    React.useEffect(() => {
        (async () => {
            const res = await fetch(process.env.REACT_APP_API_URL + '/v1/latest-routes/')
            setRoutes(await res.json())
            if (!document.lazyLoadInstance) {
              document.lazyLoadInstance = new LazyLoad();
            }
            document.lazyLoadInstance.update();
        })()
    }, [])
    
    return (
      <>
        <h3>Latest Routes</h3>
        <div className="container" style={{textAlign: 'left'}}>
            { routes === false && <div style={{textAlign: 'center'}}><span><i class="fa fa-spinner fa-spin"></i> Loading</span></div>}
            { routes && (!routes.length ? 
               (
                  <div style={{textAlign: 'center'}}><span>No routes have been yet uploaded...</span></div>
                ) : (
                  <div className="row">
                    {routes.map(r=>(
                    <div key={r.id} className="col-12 col-md-4">
                      <div className="card">
                        <Link to={'/routes/'+r.id}><img className="card-img-top lazyload" src="http://placehold.it/256x256/CCCCCC/FFFFFF&amp;text=Loading..." data-src={r.map_thumbnail_url} alt="map thumbnail" width="500" height="auto"></img></Link>
                        <div className="card-body">
                          <h5 className="card-title"><span className={("flag-icon flag-icon-"+r.country.toLowerCase())}></span> {r.name}</h5>
                          <p className="card-text">By <Link to={'/athletes/'+r.athlete.username}>{r.athlete.first_name} {r.athlete.last_name}</Link></p>
                          <p className="card-text">{moment(r.start_time).utcOffset(r.tz).format('dddd, MMMM Do YYYY, HH:mm')}</p>
                        </div>
                      </div>
                    </div>))}
                  </div>
                )   
            )}
        </div>
      </>
    ) 
}

export default LatestRoute