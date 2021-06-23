/**
 * File main.js
 *
 */
 
/* Mobile Navigation */
 
( function( $ ) {
	
	var body, menuToggle, mobileHeader, mobileNavigation;
	
	var $mobile_nav = $('#mobile-navigation');
	
	var $clone_main_menu = $('#site-navigation').children().clone();
	$clone_main_menu = $clone_main_menu.removeAttr('id');
	$clone_main_menu = $clone_main_menu.addClass('mobile-menu');
	
	if ( $( ".header-bottom .social-links" ).length ) {
		var $clone_social_links = $('.header-bottom .social-links').children().clone();
		$clone_social_links = $clone_social_links.removeAttr('id');
		$clone_social_links = $clone_social_links.addClass('mobile-social-menu');
		$mobile_nav.append( $clone_main_menu, $clone_social_links );
	} else if ( $( ".header-top .social-links" ).length ) {
		var $clone_social_links = $('.header-top .social-links').children().clone();
		$clone_social_links = $clone_social_links.removeAttr('id');
		$clone_social_links = $clone_social_links.addClass('mobile-social-menu');
		$mobile_nav.append( $clone_main_menu, $clone_social_links );
	} else {
		$mobile_nav.append( $clone_main_menu );
	}

	function initMainNavigation( container ) {

		// Add dropdown toggle that displays child menu items.
		var dropdownToggle = $( '<button />', {
			'class': 'dropdown-toggle',
			'aria-expanded': false
		} );

		container.find( '.menu-item-has-children > a' ).after( dropdownToggle );

		// Toggle buttons and submenu items with active children menu items.
		container.find( '.current-menu-ancestor > button' ).addClass( 'toggled-on' );
		container.find( '.current-menu-ancestor > .sub-menu' ).addClass( 'toggled-on' );

		// Add menu items with submenus to aria-haspopup="true".
		container.find( '.menu-item-has-children' ).attr( 'aria-haspopup', 'true' );

		container.find( '.dropdown-toggle' ).click( function( e ) {
			var _this            = $( this ),
				screenReaderSpan = _this.find( '.screen-reader-text' );

			e.preventDefault();
			_this.toggleClass( 'toggled-on' );
			_this.next( '.children, .sub-menu' ).toggleClass( 'toggled-on' );

			// jscs:disable
			_this.attr( 'aria-expanded', _this.attr( 'aria-expanded' ) === 'false' ? 'true' : 'false' );
			// jscs:enable
			
		} );
	}
	initMainNavigation( $( '.mobile-navigation' ) );

	body				= $( 'body' );
	menuToggle			= $( '#menu-toggle' );
	mobileHeader		= $( '#mobile-header' );
	mobileNavigation	= $( '#mobile-navigation' );

	// Enable menuToggle.
	( function() {

		// Return early if menuToggle is missing.
		if ( ! menuToggle.length ) {
			return;
		}
				
		// Add an initial values for the attribute.
		menuToggle.add( mobileNavigation ).attr( 'aria-expanded', 'false' );

		menuToggle.on( 'click.type', function() {
			
			if( ! mobileNavigation.hasClass('active') ) {
			mobileNavigation.slideDown(400);
			mobileNavigation.addClass('active');
    		} else if( mobileNavigation.hasClass('active') ) {
			mobileNavigation.removeClass('active');
			mobileNavigation.slideUp(400);
			}
			
			body.toggleClass( 'mobile-nav-open' );
			
			// jscs:disable
			$( this ).add( mobileNavigation ).attr( 'aria-expanded', $( this ).add( mobileNavigation ).attr( 'aria-expanded' ) === 'false' ? 'true' : 'false' );
			// jscs:enable
		} );
	} )();

	// Fix sub-menus for touch devices and better focus for hidden submenu items for accessibility.
	( function() {
		if ( ! mobileNavigation.length || ! mobileNavigation.children().length ) {
			return;
		}

		// Toggle `focus` class to allow submenu access on tablets.
		function toggleFocusClassTouchScreen() {
			if ( window.innerWidth >= 960 ) {
				$( document.body ).on( 'touchstart.type', function( e ) {
					if ( ! $( e.target ).closest( '.mobile-navigation li' ).length ) {
						$( '.mobile-navigation li' ).removeClass( 'focus' );
					}
				} );
				mobileNavigation.find( '.menu-item-has-children > a' ).on( 'touchstart.type', function( e ) {
					var el = $( this ).parent( 'li' );

					if ( ! el.hasClass( 'focus' ) ) {
						e.preventDefault();
						el.toggleClass( 'focus' );
						el.siblings( '.focus' ).removeClass( 'focus' );
					}
				} );
			} else {
				mobileNavigation.find( '.menu-item-has-children > a' ).unbind( 'touchstart.type' );
			}
		}

		if ( 'ontouchstart' in window ) {
			$( window ).on( 'resize.type', toggleFocusClassTouchScreen );
			toggleFocusClassTouchScreen();
		}

		mobileNavigation.find( 'a' ).on( 'focus.type blur.type', function() {
			$( this ).parents( '.menu-item' ).toggleClass( 'focus' );
		} );
	} )();

	// Add the default ARIA attributes for the menu toggle and the navigations.
	function onResizeARIA() {
		if ( window.innerWidth < 960 ) {
			if ( menuToggle.hasClass( 'toggled-on' ) ) {
				menuToggle.attr( 'aria-expanded', 'true' );
			} else {
				menuToggle.attr( 'aria-expanded', 'false' );
			}

			if ( mobileHeader.hasClass( 'active' ) ) {
				mobileNavigation.attr( 'aria-expanded', 'true' );
			} else {
				mobileNavigation.attr( 'aria-expanded', 'false' );
			}

			menuToggle.attr( 'aria-controls', 'site-navigation' );
		} else {
			menuToggle.removeAttr( 'aria-expanded' );
			mobileNavigation.removeAttr( 'aria-expanded' );
			menuToggle.removeAttr( 'aria-controls' );
		}
	}	

} )( jQuery );


/* Search Icon Toggle effect */

jQuery(document).ready(function(){
	jQuery('.search-popup-button').click(function(){
		jQuery('.search-popup').toggleClass('active');
	});
});
