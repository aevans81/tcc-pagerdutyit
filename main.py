



<!DOCTYPE html>
<html class="   ">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    
    <title>PagerDutyCallDesk/main.py at master · eurica/PagerDutyCallDesk · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="eurica/PagerDutyCallDesk" name="twitter:title" /><meta content="Contribute to PagerDutyCallDesk development by creating an account on GitHub." name="twitter:description" /><meta content="https://avatars3.githubusercontent.com/u/51648?v=2&amp;s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars3.githubusercontent.com/u/51648?v=2&amp;s=400" property="og:image" /><meta content="eurica/PagerDutyCallDesk" property="og:title" /><meta content="https://github.com/eurica/PagerDutyCallDesk" property="og:url" /><meta content="Contribute to PagerDutyCallDesk development by creating an account on GitHub." property="og:description" />

    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="18E168BD:552F:288B2CA:53E191C5" name="octolytics-dimension-request_id" />
    

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="B60V7qU78duVPY6SYHlUsSfNtEufaR0DPsNeFj7tWIiibBJ29XjIo5OqGFdXPhG/arv8hiKTovfD/1sYcIARBw==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-d89182d94a6bd6d7503d4b07e46af03cd2636c2d.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://assets-cdn.github.com/assets/github2-d5ca6294e43a357c97e0ba8430a1ceabeeec6fc7.css" media="all" rel="stylesheet" type="text/css" />
    


    <meta http-equiv="x-pjax-version" content="133e108720ce8bf097c5ad2e364d7eed">

      
  <meta name="description" content="Contribute to PagerDutyCallDesk development by creating an account on GitHub.">


  <meta content="51648" name="octolytics-dimension-user_id" /><meta content="eurica" name="octolytics-dimension-user_login" /><meta content="3000017" name="octolytics-dimension-repository_id" /><meta content="eurica/PagerDutyCallDesk" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="3000017" name="octolytics-dimension-repository_network_root_id" /><meta content="eurica/PagerDutyCallDesk" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/eurica/PagerDutyCallDesk/commits/master.atom" rel="alternate" title="Recent Commits to PagerDutyCallDesk:master" type="application/atom+xml">

  </head>


  <body class="logged_out  env-production windows vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions">
        <a class="button primary" href="/join">Sign up</a>
      <a class="button signin" href="/login?return_to=%2Feurica%2FPagerDutyCallDesk%2Fblob%2Fmaster%2Fmain.py">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">

      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
          <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="https://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>

<div class="commandbar">
  <span class="message"></span>
  <input type="text" data-hotkey="s, /" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    
    data-repo="eurica/PagerDutyCallDesk"
  >
  <div class="display hidden"></div>
</div>

    <input type="hidden" name="nwo" value="eurica/PagerDutyCallDesk">

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target" role="button" aria-haspopup="true">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container" aria-hidden="true">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked">
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global">
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="help tooltipped tooltipped-s" aria-label="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
    </div>

  </div>
</div>



      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">


  <li>
      <a href="/login?return_to=%2Feurica%2FPagerDutyCallDesk"
    class="minibutton with-count star-button tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <span class="octicon octicon-star"></span>
    Star
  </a>

    <a class="social-count js-social-count" href="/eurica/PagerDutyCallDesk/stargazers">
      8
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2Feurica%2FPagerDutyCallDesk"
        class="minibutton with-count js-toggler-target fork-button tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-repo-forked"></span>
        Fork
      </a>
      <a href="/eurica/PagerDutyCallDesk/network" class="social-count">
        0
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/eurica" class="url fn" itemprop="url" rel="author"><span itemprop="title">eurica</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/eurica/PagerDutyCallDesk" class="js-current-repository js-repo-home-link">PagerDutyCallDesk</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders" data-issue-count-url="/eurica/PagerDutyCallDesk/issues/counts">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Code">
        <a href="/eurica/PagerDutyCallDesk" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /eurica/PagerDutyCallDesk">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped tooltipped-w" aria-label="Issues">
          <a href="/eurica/PagerDutyCallDesk/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /eurica/PagerDutyCallDesk/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class="js-issue-replace-counter"></span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
        <a href="/eurica/PagerDutyCallDesk/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g p" data-selected-links="repo_pulls /eurica/PagerDutyCallDesk/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class="js-pull-replace-counter"></span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped tooltipped-w" aria-label="Pulse">
        <a href="/eurica/PagerDutyCallDesk/pulse/weekly" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /eurica/PagerDutyCallDesk/pulse/weekly">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Graphs">
        <a href="/eurica/PagerDutyCallDesk/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /eurica/PagerDutyCallDesk/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

              <div class="only-with-full-nav">
                
  
<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="input-group">
    <input type="text" class="input-mini input-monospace js-url-field"
           value="https://github.com/eurica/PagerDutyCallDesk.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/eurica/PagerDutyCallDesk.git" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="input-group">
    <input type="text" class="input-mini input-monospace js-url-field"
           value="https://github.com/eurica/PagerDutyCallDesk" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/eurica/PagerDutyCallDesk" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>


  <a href="http://windows.github.com" class="minibutton sidebar-button" title="Save eurica/PagerDutyCallDesk to your computer and use it in GitHub Desktop." aria-label="Save eurica/PagerDutyCallDesk to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>

                <a href="/eurica/PagerDutyCallDesk/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download eurica/PagerDutyCallDesk as a zip file"
                   title="Download eurica/PagerDutyCallDesk as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          

<a href="/eurica/PagerDutyCallDesk/blob/8b730ed3565533583678e2f08d987352c71835c5/main.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:f32d832d8513b085263afe6cb15c1b76 -->

<div class="file-navigation">
  
<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/eurica/PagerDutyCallDesk/blob/master/main.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="button-group right">
    <a href="/eurica/PagerDutyCallDesk/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button class="js-zeroclipboard minibutton zeroclipboard-button"
          data-clipboard-text="main.py"
          aria-label="Copy to clipboard"
          data-copied-hint="Copied!">
      <span class="octicon octicon-clippy"></span>
    </button>
  </div>

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/eurica/PagerDutyCallDesk" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">PagerDutyCallDesk</span></a></span></span><span class="separator"> / </span><strong class="final-path">main.py</strong>
  </div>
</div>


  <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/eurica/PagerDutyCallDesk/contributors/master/main.py">
    Fetching contributors…

    <div class="participation">
      <p class="loader-loading"><img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
      <p class="loader-error">Cannot retrieve contributors at this time</p>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
          <span>99 lines (87 sloc)</span>
          <span class="meta-divider"></span>
        <span>4.241 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
          <a href="/eurica/PagerDutyCallDesk/raw/master/main.py" class="minibutton " id="raw-url">Raw</a>
            <a href="/eurica/PagerDutyCallDesk/blame/master/main.py" class="minibutton js-update-url-with-hash">Blame</a>
          <a href="/eurica/PagerDutyCallDesk/commits/master/main.py" class="minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->

          <a class="octicon-button tooltipped tooltipped-nw"
             href="http://windows.github.com" aria-label="Open this file in GitHub for Windows">
              <span class="octicon octicon-device-desktop"></span>
          </a>

            <a class="octicon-button disabled tooltipped tooltipped-w" href="#"
               aria-label="You must be signed in to make or propose changes"><span class="octicon octicon-pencil"></span></a>

          <a class="octicon-button danger disabled tooltipped tooltipped-w" href="#"
             aria-label="You must be signed in to make or propose changes">
          <span class="octicon octicon-trashcan"></span>
        </a>
      </div><!-- /.actions -->
    </div>
      
  <div class="blob-wrapper data type-python">
       <table class="file-code file-diff tab-size-8 js-file-line-container">
         <tr class="file-code-line">
           <td class="blob-line-nums">
             <span id="L1" class="js-line-number">1</span>
<span id="L2" class="js-line-number">2</span>
<span id="L3" class="js-line-number">3</span>
<span id="L4" class="js-line-number">4</span>
<span id="L5" class="js-line-number">5</span>
<span id="L6" class="js-line-number">6</span>
<span id="L7" class="js-line-number">7</span>
<span id="L8" class="js-line-number">8</span>
<span id="L9" class="js-line-number">9</span>
<span id="L10" class="js-line-number">10</span>
<span id="L11" class="js-line-number">11</span>
<span id="L12" class="js-line-number">12</span>
<span id="L13" class="js-line-number">13</span>
<span id="L14" class="js-line-number">14</span>
<span id="L15" class="js-line-number">15</span>
<span id="L16" class="js-line-number">16</span>
<span id="L17" class="js-line-number">17</span>
<span id="L18" class="js-line-number">18</span>
<span id="L19" class="js-line-number">19</span>
<span id="L20" class="js-line-number">20</span>
<span id="L21" class="js-line-number">21</span>
<span id="L22" class="js-line-number">22</span>
<span id="L23" class="js-line-number">23</span>
<span id="L24" class="js-line-number">24</span>
<span id="L25" class="js-line-number">25</span>
<span id="L26" class="js-line-number">26</span>
<span id="L27" class="js-line-number">27</span>
<span id="L28" class="js-line-number">28</span>
<span id="L29" class="js-line-number">29</span>
<span id="L30" class="js-line-number">30</span>
<span id="L31" class="js-line-number">31</span>
<span id="L32" class="js-line-number">32</span>
<span id="L33" class="js-line-number">33</span>
<span id="L34" class="js-line-number">34</span>
<span id="L35" class="js-line-number">35</span>
<span id="L36" class="js-line-number">36</span>
<span id="L37" class="js-line-number">37</span>
<span id="L38" class="js-line-number">38</span>
<span id="L39" class="js-line-number">39</span>
<span id="L40" class="js-line-number">40</span>
<span id="L41" class="js-line-number">41</span>
<span id="L42" class="js-line-number">42</span>
<span id="L43" class="js-line-number">43</span>
<span id="L44" class="js-line-number">44</span>
<span id="L45" class="js-line-number">45</span>
<span id="L46" class="js-line-number">46</span>
<span id="L47" class="js-line-number">47</span>
<span id="L48" class="js-line-number">48</span>
<span id="L49" class="js-line-number">49</span>
<span id="L50" class="js-line-number">50</span>
<span id="L51" class="js-line-number">51</span>
<span id="L52" class="js-line-number">52</span>
<span id="L53" class="js-line-number">53</span>
<span id="L54" class="js-line-number">54</span>
<span id="L55" class="js-line-number">55</span>
<span id="L56" class="js-line-number">56</span>
<span id="L57" class="js-line-number">57</span>
<span id="L58" class="js-line-number">58</span>
<span id="L59" class="js-line-number">59</span>
<span id="L60" class="js-line-number">60</span>
<span id="L61" class="js-line-number">61</span>
<span id="L62" class="js-line-number">62</span>
<span id="L63" class="js-line-number">63</span>
<span id="L64" class="js-line-number">64</span>
<span id="L65" class="js-line-number">65</span>
<span id="L66" class="js-line-number">66</span>
<span id="L67" class="js-line-number">67</span>
<span id="L68" class="js-line-number">68</span>
<span id="L69" class="js-line-number">69</span>
<span id="L70" class="js-line-number">70</span>
<span id="L71" class="js-line-number">71</span>
<span id="L72" class="js-line-number">72</span>
<span id="L73" class="js-line-number">73</span>
<span id="L74" class="js-line-number">74</span>
<span id="L75" class="js-line-number">75</span>
<span id="L76" class="js-line-number">76</span>
<span id="L77" class="js-line-number">77</span>
<span id="L78" class="js-line-number">78</span>
<span id="L79" class="js-line-number">79</span>
<span id="L80" class="js-line-number">80</span>
<span id="L81" class="js-line-number">81</span>
<span id="L82" class="js-line-number">82</span>
<span id="L83" class="js-line-number">83</span>
<span id="L84" class="js-line-number">84</span>
<span id="L85" class="js-line-number">85</span>
<span id="L86" class="js-line-number">86</span>
<span id="L87" class="js-line-number">87</span>
<span id="L88" class="js-line-number">88</span>
<span id="L89" class="js-line-number">89</span>
<span id="L90" class="js-line-number">90</span>
<span id="L91" class="js-line-number">91</span>
<span id="L92" class="js-line-number">92</span>
<span id="L93" class="js-line-number">93</span>
<span id="L94" class="js-line-number">94</span>
<span id="L95" class="js-line-number">95</span>
<span id="L96" class="js-line-number">96</span>
<span id="L97" class="js-line-number">97</span>
<span id="L98" class="js-line-number">98</span>
<span id="L99" class="js-line-number">99</span>

           </td>
           <td class="blob-line-code"><div class="code-body highlight"><pre><div class='line js-file-line' id='LC1'><span class="c"># PagerDuty incidents triggered by phone: </span></div><div class='line js-file-line' id='LC2'><span class="kn">import</span> <span class="nn">logging</span></div><div class='line js-file-line' id='LC3'><span class="kn">from</span> <span class="nn">urllib2</span> <span class="kn">import</span> <span class="n">Request</span><span class="p">,</span> <span class="n">urlopen</span><span class="p">,</span> <span class="n">URLError</span><span class="p">,</span> <span class="n">HTTPError</span></div><div class='line js-file-line' id='LC4'><span class="kn">import</span> <span class="nn">urllib</span></div><div class='line js-file-line' id='LC5'><span class="kn">from</span> <span class="nn">django.utils</span> <span class="kn">import</span> <span class="n">simplejson</span> <span class="k">as</span> <span class="n">json</span></div><div class='line js-file-line' id='LC6'><span class="kn">from</span> <span class="nn">google.appengine.ext</span> <span class="kn">import</span> <span class="n">webapp</span></div><div class='line js-file-line' id='LC7'><span class="kn">from</span> <span class="nn">google.appengine.ext.webapp</span> <span class="kn">import</span> <span class="n">util</span></div><div class='line js-file-line' id='LC8'><br></div><div class='line js-file-line' id='LC9'><span class="n">SERVICE_KEY</span> <span class="o">=</span> <span class="s">&quot;2fad977c7c24416b983296a4bed7d96b&quot;</span></div><div class='line js-file-line' id='LC10'><br></div><div class='line js-file-line' id='LC11'><span class="c">#Half of the code is just dedicated to URL shortening, so that we can fit the MP3&#39;s URL in an SMS:</span></div><div class='line js-file-line' id='LC12'><span class="k">def</span> <span class="nf">shorten</span><span class="p">(</span><span class="n">url</span><span class="p">):</span></div><div class='line js-file-line' id='LC13'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">gurl</span> <span class="o">=</span> <span class="s">&#39;http://goo.gl/api/url?url=</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">urllib</span><span class="o">.</span><span class="n">unquote</span><span class="p">(</span><span class="n">url</span><span class="p">)</span></div><div class='line js-file-line' id='LC14'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">req</span> <span class="o">=</span> <span class="n">Request</span><span class="p">(</span><span class="n">gurl</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="s">&#39;&#39;</span><span class="p">)</span></div><div class='line js-file-line' id='LC15'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">req</span><span class="o">.</span><span class="n">add_header</span><span class="p">(</span><span class="s">&#39;User-Agent&#39;</span><span class="p">,</span> <span class="s">&#39;toolbar&#39;</span><span class="p">)</span></div><div class='line js-file-line' id='LC16'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Shortening &#39;</span> <span class="o">+</span> <span class="n">gurl</span><span class="p">)</span></div><div class='line js-file-line' id='LC17'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line js-file-line' id='LC18'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">res</span> <span class="o">=</span> <span class="n">urlopen</span><span class="p">(</span><span class="n">req</span><span class="p">)</span></div><div class='line js-file-line' id='LC19'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">results</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">res</span><span class="p">)</span></div><div class='line js-file-line' id='LC20'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span> <span class="n">res</span><span class="o">.</span><span class="n">code</span> <span class="p">)</span></div><div class='line js-file-line' id='LC21'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="n">HTTPError</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span> <span class="c">#triggers on HTTP code 201</span></div><div class='line js-file-line' id='LC22'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span> <span class="n">e</span><span class="o">.</span><span class="n">code</span> <span class="p">)</span></div><div class='line js-file-line' id='LC23'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">error_content</span> <span class="o">=</span> <span class="n">e</span><span class="o">.</span><span class="n">read</span><span class="p">()</span> </div><div class='line js-file-line' id='LC24'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">results</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">JSONDecoder</span><span class="p">()</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">error_content</span><span class="p">)</span></div><div class='line js-file-line' id='LC25'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line js-file-line' id='LC26'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">results</span><span class="p">[</span><span class="s">&#39;short_url&#39;</span><span class="p">]</span></div><div class='line js-file-line' id='LC27'><br></div><div class='line js-file-line' id='LC28'><span class="c"># Outbput the TwilML to record a message and pass it to /record</span></div><div class='line js-file-line' id='LC29'><span class="k">class</span> <span class="nc">CallHandler</span><span class="p">(</span><span class="n">webapp</span><span class="o">.</span><span class="n">RequestHandler</span><span class="p">):</span></div><div class='line js-file-line' id='LC30'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line js-file-line' id='LC31'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">response</span> <span class="o">=</span> <span class="p">(</span><span class="s">&quot;&lt;?xml version=</span><span class="se">\&quot;</span><span class="s">1.0</span><span class="se">\&quot;</span><span class="s"> encoding=</span><span class="se">\&quot;</span><span class="s">UTF-8</span><span class="se">\&quot;</span><span class="s">?&gt;&quot;</span></div><div class='line js-file-line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&lt;Response&gt;&lt;Say&gt;Leave a message at the beep.&lt;/Say&gt;&quot;</span></div><div class='line js-file-line' id='LC33'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&lt;Record action=</span><span class="se">\&quot;</span><span class="s">http://pdtestthrough.appspot.com/record</span><span class="se">\&quot;</span><span class="s"> method=</span><span class="se">\&quot;</span><span class="s">GET</span><span class="se">\&quot;</span><span class="s">/&gt;&quot;</span></div><div class='line js-file-line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&lt;Say&gt;I did not receive a recording&lt;/Say&gt;&lt;/Response&gt;&quot;</span><span class="p">)</span></div><div class='line js-file-line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">response</span><span class="o">.</span><span class="n">out</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">response</span><span class="p">)</span></div><div class='line js-file-line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Recieved CALL &#39;</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">request</span><span class="o">.</span><span class="n">query_string</span><span class="p">)</span></div><div class='line js-file-line' id='LC37'><br></div><div class='line js-file-line' id='LC38'><span class="c"># Shorten the URL and trigger a PD incident with it</span></div><div class='line js-file-line' id='LC39'><span class="k">class</span> <span class="nc">RecordHandler</span><span class="p">(</span><span class="n">webapp</span><span class="o">.</span><span class="n">RequestHandler</span><span class="p">):</span></div><div class='line js-file-line' id='LC40'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line js-file-line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">response</span> <span class="o">=</span> <span class="p">(</span><span class="s">&quot;&lt;?xml version=</span><span class="se">\&quot;</span><span class="s">1.0</span><span class="se">\&quot;</span><span class="s"> encoding=</span><span class="se">\&quot;</span><span class="s">UTF-8</span><span class="se">\&quot;</span><span class="s">?&gt;&lt;Response&gt;&lt;Say&gt;Thanks.  Directing your message to the agent on call.&lt;/Say&gt;&lt;/Response&gt;&quot;</span><span class="p">)</span></div><div class='line js-file-line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">response</span><span class="o">.</span><span class="n">out</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">response</span><span class="p">)</span></div><div class='line js-file-line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Recieved RECORDING: &#39;</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">request</span><span class="o">.</span><span class="n">query_string</span><span class="p">)</span></div><div class='line js-file-line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">recUrl</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&quot;RecordingUrl&quot;</span><span class="p">)</span></div><div class='line js-file-line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">phonenumber</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&quot;From&quot;</span><span class="p">)</span></div><div class='line js-file-line' id='LC46'><br></div><div class='line js-file-line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Recieved RECORDING &#39;</span> <span class="o">+</span> <span class="n">recUrl</span><span class="p">)</span></div><div class='line js-file-line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span><span class="p">(</span><span class="n">recUrl</span><span class="p">):</span></div><div class='line js-file-line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Found recording!&#39;</span><span class="p">)</span></div><div class='line js-file-line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">recUrl</span> <span class="o">=</span> <span class="n">recUrl</span> <span class="o">+</span> <span class="s">&#39;.mp3&#39;</span> <span class="c">#There&#39;s better support for URLs that include the .mp3</span></div><div class='line js-file-line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line js-file-line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">recUrl</span> <span class="o">=</span> <span class="s">&quot;https://github.com/eurica/PagerDutyCallDesk/&quot;</span> <span class="c"># I don&#39;t know what I should do with incidents that don&#39;t include an MP3</span></div><div class='line js-file-line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">phonenumber</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></div><div class='line js-file-line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shrten</span> <span class="o">=</span> <span class="s">&quot;Error&quot;</span></div><div class='line js-file-line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line js-file-line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line js-file-line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shrten</span> <span class="o">=</span> <span class="n">shorten</span><span class="p">(</span><span class="n">recUrl</span><span class="p">)</span></div><div class='line js-file-line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="n">HTTPError</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span></div><div class='line js-file-line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shrten</span> <span class="o">=</span> <span class="s">&quot;HTTPError&quot;</span></div><div class='line js-file-line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logging</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span> <span class="n">e</span><span class="o">.</span><span class="n">code</span> <span class="p">)</span></div><div class='line js-file-line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="n">URLError</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span></div><div class='line js-file-line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">shrten</span> <span class="o">=</span> <span class="s">&quot;URLError&quot;</span></div><div class='line js-file-line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logging</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">reason</span><span class="p">)</span> </div><div class='line js-file-line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line js-file-line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;Shortened to: &#39;</span> <span class="o">+</span> <span class="n">shrten</span><span class="p">)</span></div><div class='line js-file-line' id='LC66'>&nbsp;&nbsp;</div><div class='line js-file-line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Obviously use your own key:</span></div><div class='line js-file-line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">incident</span> <span class="o">=</span> <span class="s">&#39;{&quot;service_key&quot;: &quot;</span><span class="si">%s</span><span class="s">&quot;,&quot;incident_key&quot;: &quot;</span><span class="si">%s</span><span class="s">&quot;,&quot;event_type&quot;: &quot;trigger&quot;,&quot;description&quot;: &quot;</span><span class="si">%s</span><span class="s"> </span><span class="si">%s</span><span class="s">&quot;}&#39;</span><span class="o">%</span><span class="p">(</span><span class="n">SERVICE_KEY</span><span class="p">,</span><span class="n">shrten</span><span class="p">,</span><span class="n">shrten</span><span class="p">,</span><span class="n">phonenumber</span><span class="p">)</span></div><div class='line js-file-line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line js-file-line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">r</span> <span class="o">=</span> <span class="n">Request</span><span class="p">(</span><span class="s">&quot;http://events.pagerduty.com/generic/2010-04-15/create_event.json&quot;</span><span class="p">,</span> <span class="n">incident</span><span class="p">)</span> <span class="c">#Note according to the API this should be retried on failure</span></div><div class='line js-file-line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">results</span> <span class="o">=</span> <span class="n">urlopen</span><span class="p">(</span><span class="n">r</span><span class="p">)</span></div><div class='line js-file-line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="n">incident</span><span class="p">)</span></div><div class='line js-file-line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="n">results</span><span class="p">)</span></div><div class='line js-file-line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="n">HTTPError</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span></div><div class='line js-file-line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logging</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span> <span class="n">e</span><span class="o">.</span><span class="n">code</span> <span class="p">)</span></div><div class='line js-file-line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="n">URLError</span><span class="p">,</span> <span class="n">e</span><span class="p">:</span></div><div class='line js-file-line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">logging</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">reason</span><span class="p">)</span>   </div><div class='line js-file-line' id='LC78'><br></div><div class='line js-file-line' id='LC79'><span class="c"># A somewhat descriptive index page</span></div><div class='line js-file-line' id='LC80'><span class="k">class</span> <span class="nc">IndexHandler</span><span class="p">(</span><span class="n">webapp</span><span class="o">.</span><span class="n">RequestHandler</span><span class="p">):</span></div><div class='line js-file-line' id='LC81'>&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line js-file-line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">response</span> <span class="o">=</span> <span class="p">(</span><span class="s">&quot;&lt;html&gt;&lt;h1&gt;Trigger a &lt;a href=&#39;http://www.pagerduty.com&#39;&gt;PagerDuty&lt;/a&gt; incident from a phone call&lt;/h1&gt;&lt;ul&gt;&quot;</span></div><div class='line js-file-line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&lt;li&gt;&lt;a href=&#39;http://blog.pagerduty.com/2012/02/triggering-an-alert-from-a-phone-call&#39;&gt;About&lt;/a&gt;&quot;</span></div><div class='line js-file-line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&lt;li&gt;&lt;a href=&#39;https://github.com/eurica/PagerDutyCallDesk/&#39;&gt;GitHub page&lt;/a&gt;&quot;</span></div><div class='line js-file-line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&lt;li&gt;&lt;a href=&#39;/call&#39;&gt;/call&lt;/a&gt; (returns XML)&quot;</span></div><div class='line js-file-line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&lt;li&gt;&lt;a href=&#39;/record?RecordingUrl=http%3A</span><span class="si">%2F%2F</span><span class="s">api.twilio.com</span><span class="si">%2F</span><span class="s">2010-04-01</span><span class="si">%2F</span><span class="s">Accounts</span><span class="si">%2F</span><span class="s">ACfdf710462c058abf3a987f393e8e9bc8</span><span class="si">%2F</span><span class="s">Recordings</span><span class="si">%2F</span><span class="s">RE6f523cd7734fa86e56e5ef0ea5ffd4cf&#39;&gt;/record&lt;/a&gt; (test with &#39;Hey this is Jim...&#39;)&quot;</span></div><div class='line js-file-line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;&lt;/ul&gt;Remember to change the application identifier and the service API key, or else you&#39;ll just alert me :)&lt;/html&gt;&quot;</span><span class="p">)</span></div><div class='line js-file-line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">response</span><span class="o">.</span><span class="n">out</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">response</span><span class="p">)</span></div><div class='line js-file-line' id='LC89'><br></div><div class='line js-file-line' id='LC90'><span class="k">def</span> <span class="nf">main</span><span class="p">():</span></div><div class='line js-file-line' id='LC91'>&nbsp;&nbsp;<span class="n">application</span> <span class="o">=</span> <span class="n">webapp</span><span class="o">.</span><span class="n">WSGIApplication</span><span class="p">([</span></div><div class='line js-file-line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;/call&#39;</span><span class="p">,</span> <span class="n">CallHandler</span><span class="p">),</span></div><div class='line js-file-line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;/record&#39;</span><span class="p">,</span> <span class="n">RecordHandler</span><span class="p">),</span></div><div class='line js-file-line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="s">&#39;/&#39;</span><span class="p">,</span> <span class="n">IndexHandler</span><span class="p">)],</span></div><div class='line js-file-line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">debug</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span></div><div class='line js-file-line' id='LC96'>&nbsp;&nbsp;<span class="n">util</span><span class="o">.</span><span class="n">run_wsgi_app</span><span class="p">(</span><span class="n">application</span><span class="p">)</span></div><div class='line js-file-line' id='LC97'><br></div><div class='line js-file-line' id='LC98'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span></div><div class='line js-file-line' id='LC99'>&nbsp;&nbsp;<span class="n">main</span><span class="p">()</span></div></pre></div></td>
         </tr>
       </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.03905s from github-fe122-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents js-suggester-field" placeholder=""></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-12d5fda141e78e513749dddbc56445fe172cbd9a.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-a1b27a14e6e11ca95a737934e426decbc4db3704.js" type="text/javascript"></script>
      
      
        <script async src="https://www.google-analytics.com/analytics.js"></script>
  </body>
</html>

