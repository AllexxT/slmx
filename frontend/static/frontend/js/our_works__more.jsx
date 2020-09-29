const { Fragment, useState, useEffect } = React;

const OneMoreGallery = ({ galleryItem }) => {
  useEffect(() => {
    if (!document.galleriesIsLoaded) {
      var galleries2 = $(".ad-gallery").adGallery();
      document.galleriesIsLoaded = true;
    }
  }, []);
  return (
    <div className="our-works">
      <div className="our-works__gallery">
        <div id="ad-gallery" className="ad-gallery">
          <div className="ad-image-wrapper"> </div>
          <div className="ad-controls"> </div>
          <div className="ad-nav">
            <div className="ad-thumbs">
              <ul className="ad-thumb-list">
                {galleryItem.images.map((img, key) => (
                  <li key={key}>
                    <a href={img.image}>
                      <img src={img.thumbnail} width="160" height="107" />
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div className="g-description">
        <div className="g-description__wrapper">
          <div className="g-description__title">
            <h2>{galleryItem.title}</h2>
          </div>
          <div className="g-description__address">{galleryItem.address}</div>
          <div
            className="g-description__address-text"
            dangerouslySetInnerHTML={{ __html: galleryItem.description }}
          ></div>
        </div>
      </div>
    </div>
  );
};

const More = () => {
  console.log("render");

  const [galleries, setGalleries] = useState({
    preloader: false,
    items: [],
  });
  const [counter, setCounter] = useState({
    last: 3,
    step: 4,
  });

  //   prevent loading copies of 'ad-preloads'(almost)
  document.galleriesIsLoaded = false;

  const getMoreGalleries = () => {
    setCounter({ ...counter, step: counter.step + 1 });
    axios
      .get("", {
        params: {
          last: counter.last,
          nxt: counter.step,
        },
      })
      .then((response) => {
        setGalleries({ preloader: false, items: response.data.more });
      })
      .catch((error) => console.log(error));
  };
  console.log(counter);
  return (
    <Fragment>
      {galleries.items.map((item, key) => (
        <OneMoreGallery galleryItem={item} key={key} />
      ))}
      <button onClick={() => getMoreGalleries()}>показать еще</button>
    </Fragment>
  );
};

const RootMore = () => {
  return (
    <More/>
  )
}

ReactDOM.render(<RootMore />, document.getElementById("more"));
